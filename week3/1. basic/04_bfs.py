"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """

    # 방문 순서 기록용
    visited = []
    # 방문한 놈인지 확인하기 위한 친구
    isVisited = [False] * len(graph)
    
    # TODO: 큐 생성 및 시작 정점 추가
    queue = deque([start])

    # 시작하는 놈은 방문한 놈임!
    visited.append(start)
    isVisited[start] = True
    
    # TODO: 큐가 빌 때까지 반복
    while queue:
        # 큐에서 이웃 확인할 정점 꺼내기
        node = queue.popleft()

        # 이웃 정점들 확인
        for neighbor in graph[node]:
            # # 이렇게 하시면 시간복잡도가 O(n)이라 터지십니다
            # if neighbor not in visited:
            if not isVisited[neighbor]:
                # 방문 안 한 놈이면 큐에 추가
                isVisited[neighbor] = True
                visited.append(neighbor)
                queue.append(neighbor)
    
    return visited

# 큐 안 쓰겠다고 온몸비틀기 하지 말고 걍 얌전히 큐 쓰길 바람

def bfs_without_queue(graph, start):
    visited = []
    # 방문한 놈인지 확인하기 위한 친구
    isVisited = [False] * len(graph) 
    
    # 큐 대신 '현재 층'을 담을 바구니 준비
    current_basket = [start]

    # 시작하는 놈은 방문한 놈임!
    visited.append(start)
    isVisited[start] = True
    
    # 바구니가 빌 때까지(더 이상 파 내려갈 층이 없을 때까지) 반복
    while current_basket:
        next_basket = []  # 다음 층(이웃들)을 담아둘 새 바구니
        
        # 큐에서 popleft()로 하나씩 빼는 대신, 현재 층의 노드들을 한 번에 싹 훑기
        for node in current_basket:
            
            # 이웃 정점들 확인
            for neighbor in graph[node]:
                if not isVisited[neighbor]:
                    # 방문 안 한 놈이면 다음 바구니에 추가
                    isVisited[neighbor] = True
                    visited.append(neighbor)
                    next_basket.append(neighbor)  # 큐의 append 역할
        
        # 현재 층을 다 훑었으니, 바구니를 다음 층으로 통째로 교체
        current_basket = next_basket
    
    return visited


# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")

