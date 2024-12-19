package test;

import java.util.LinkedList;
import java.util.Queue;

public class Main {
	
	public static void main(String[] args) {
		
		// 그래프를 2차원 배열로 표현
        // 인덱스와 노드를 일치 시키기 위해 0은 저장하지 않음
        // 1번 인덱스 = 1번 노드, 배뎔의 값은 연결된 노드
        int[][] graph = {{}, {2,3,7}, {1,3,5}, {1,2}, {6,8}, {2}, {4,7,8}, {1,6}, {4,6}};
        
        // 방문정보
        boolean[] visit = new boolean[9];
        System.out.println("너비우선탐색 결과");
        System.out.println(bfs(1, graph, visit));
        // 예상 결과값 : 1 -> 2 -> 3 -> 7 -> 5 -> 6 -> 4 -> 8 ->
        
        visit = new boolean[9];
        System.out.println("깊이우선탐색 결과");
        dfs(1, graph, visit);
    }

	// BFS함수		 	시작 노드, 	배열,			방문정보
    static String bfs(int start, int[][] graph, boolean[] visit) {
        
    	// 문자열 더하기 연산을 효율적으로 하기 위함
    	StringBuilder sb = new StringBuilder();
    	
    	// 정수타입의 큐 선언
        Queue<Integer> queue = new LinkedList<Integer>();
        
        // 큐에 시작점 추가 (offer: 예외발생X)
        queue.offer(start);
        
        // 방문 표시
        visit[start] = true;
        
        // 큐가 비어있을 때까지 반복
        while (!queue.isEmpty()) {
        	// == q.popleft();
            int node = queue.poll();
            
            sb.append(node + " -> ");
            
            // 큐에서 꺼낸 노드와 연결된 간선 체크
            for (int i = 0; i < graph[node].length; i++) {
                int temp = graph[node][i];
                // 방문하지 않았으면 방문처리 후에 큐에 삽입
                if (!visit[temp]) {
                    visit[temp] = true;
                    queue.offer(temp);
                }
            }
        }
        return sb.toString();
    }
    
    static void dfs(int nodeIndex, int[][] graph, boolean[] visit) {
    	// 방문 표시
    	visit[nodeIndex] = true;
    	
    	System.out.print(nodeIndex + " -> ");
    	
    	// ==> for node in graph[nodeIndex]:
    	for (int node : graph[nodeIndex]) {
    		// 미방문 시 깊이 우선 탐색을 위해 재귀호출
    		if (!visit[node]) {
    			dfs(node, graph, visit);
    		}
    	}
    }
}
