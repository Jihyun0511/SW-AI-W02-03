"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

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
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 재귀로 구현
- 방문 체크 필요
- 깊이 우선으로 방문
"""

def dfs(graph, start, visited=None):
    """
    깊이 우선 탐색 (재귀)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
    # TODO: visited가 None이면 초기화
    if visited is None: visited = []
    
    # TODO: 현재 정점 방문
    visited.append(start)
    
    # TODO: 인접한 정점들에 대해 재귀
    ## 방문하지 않은 정점이면 재귀 호출
    for v in graph[start]:
        if v not in visited:
            dfs(graph, v, visited)
    
    return visited

# 내부함수로 구현
## 내부함수의 유무가 딱히 성능차이로 이어지지는 않는다
def dfs_better(graph, start, visited=None):
    if visited is None: visited = []

    # 아까 bfs 풀 때는 배열[그래프길이]=False 해놓고 set 쓴 이유:
    ## 정점 이름이 연속된 숫자가 아니면... 10, 20, 30 따위면
    ## 3개짜리 배열 만들어놓고 배열[10] 해서 터질 수도...
    visited_set = set(visited)

    def dfs_helper(node):
        visited.append(node)
        visited_set.add(node)
        
        for v in graph[node]:
            # set은 내부적으로 해시테이블이라 찾을 때 시간복잡도가 O(1)
            if v not in visited_set:
                dfs_helper(v)

    dfs_helper(start)

    return visited

## 스택으로 구현?
## 하기싫음.....

    
# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


