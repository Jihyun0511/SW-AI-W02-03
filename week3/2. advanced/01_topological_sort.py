"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # 초기화 안 했는데 문제 생기나? 일단 둠
    ## 뻗대지 말고 초기화 합시다
    graph= {i: [] for i in range (vertices)} # 그래프
    in_degree= [0] * vertices # 진입 차수

    for u, v in edges:
        graph[u].append(v) # 그래프 생성중...
        in_degree[v] += 1 # 진입 차수 더해줌


    # 시작 정점 찾기...
    ## 여러 개일수도 있으므로 하나로 정하지 않고 걍 조건 맞는 놈들 다 큐에 넣으셈!!!
    queue= deque() # 이렇게 걍 빈 큐 만들수도 있었군... 뭘 넣어줘야 한다고 생각했음

    for i in range(vertices):
        if in_degree[i] == 0:
            queue.append(i)

    # 결과용... 방문 순서용 리스트
    result = []

    # 돌려돌려
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            # 진입 차수 하나씩 깎아줍시다...
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
