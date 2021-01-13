# map =   [[0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0]]

# Configuration 열파일정보
# Map 파일에서 맵가져옴
# BFS 알고리즘
# Run 실행


class Configuration:
    """ 파일에서("BFS_Practice.ini") 기본 설정을 가져오는 클래스"""
    def __init__(self):
        config = self.configuration()
        self.fname = config['FILENAME']
        self.encoding = config['ENCODING']

    def configuration(self):
        result = {}
        with open("BFS_Practice.ini","r") as f:
            lines = f.readlines()
            for line in lines:
                key, value = line.split("=")
                key = key.strip()
                value = value.strip()
                result[key] = value

        return result

class Map:
    def __init__(self):
        self.config = Configuration()
        self.map = self.get_map(self.config.fname)

    def get_map(self,fname):
        map = []
        with open(fname,"r",encoding="UTF-8-SIG") as f:
            lines = f.readlines()
            for line in lines:
                values = [ int(value) for value in line.split(",")]
                map.append(values)

        return map

    def __str__(self):
        result = ""
        for line in self.map:
            for value in line:
                result += f"{value},"
            result += "\n"
        return result


class Run:
    def __init__(self):
        take_map = Map()
        self.map = take_map.map
        self.result = []

    def run(self):
        index = self.select_algorism()
        if index:
            self.result = self.algorism(index)


    def select_algorism(self):
        print("1번 BFS 2번 DFS 알고리즘 입니다. 이후 확장 예정입니다.")
        ans = int(input("선택 알고리즘 : "))
        if 1<= ans <= 2:
            return ans
        return False

    def algorism(self,index):
        if index == 1:
            calc = BFS(self.map)
            calc.print_result()
        elif index == 2:
            calc = DFS(self.map)
            calc.print_result()
        else:
            return []

        return calc.result

    def __str__(self):
        return f"알고리즘을 테스트하는 실행파일 입니다.\n지난 정답은 {self.result}입니다."


class PathFindAlgorism:
    def __init__(self,map):
        self.map = map
        self.result = self.calc()
        
    def calc(self):
        
        pass
        
    def print_result(self):

        print(f"결과는 {self.result} 입니다.")



class DFS(PathFindAlgorism):

    def calc(self):
        n = len(self.map)
        visited = [0]
        print(visited)

        for i,value in enumerate(self.map[visited[0]]):
            if value == 1 and i not in visited:
                visited.append(i)
                visited = self.dfs_subcalc(i,visited)

        return visited

    def dfs_subcalc(self,node,visited):
        for i,value in enumerate(self.map[node]):
            if value == 1 and i not in visited:
                visited.append(i)
                visited = self.dfs_subcalc(i,visited)

        return visited

    

class BFS(PathFindAlgorism):

    def calc(self):
        result = []
        n = len(self.map)
        queue = [0]

        while queue:
            q = queue.pop(0)
            result.append(q)
            # for i,value in enumerate(self.map[q]):
            #     if value == 1 and i not in queue and i not in result:
            #         queue.append(i)
            queue.extend( [ i for i,value in enumerate(self.map[q])\
                 if value == 1 and i not in queue and i not in result])

        return result

    

def main():
    result = Run()
    result.run()


main()