
class Question:
    """ 
        filepath            => file_path
        question_filepath   => sol_file_path
        self.input          : 예제 입력 값(라인별 출력)
        self.answer         : 예제 정답 값

        How to Use :

        def my_solution():
            answer = q.input()
            return answer 

        q = Question(file_path)
        q.solution = my_solution
        print(q.submit())

    """
    def __init__(self,file_path):
        self.fpath = file_path
        self.input = self.input
        self.input_gen = self.input_generator()
        self.spath = "sol_"+file_path
        self.answer = self.read(self.spath)

    def input_generator(self):
        lines = ""
        with open(self.fpath,"r") as f:
            lines = f.readlines()

        for line in lines:
            yield line.strip()

    def input(self):
        try:
            line = next(self.input_gen)
            return line
        except:
            raise EOFError

    def read(self,fpath):
        with open(fpath,"r") as f:
            lines = f.read().strip()

        if lines.isnumeric():
            return int(lines)
        return lines

    def __repr__(self):
        return self.fpath


class Questions:
    """
        
        file_paths = ["ex1.txt" , "ex2.txt"]

        def sol(line):
            print("input:",line.input())
            print("input:",line.input())
            return 3
        # help(Question)
        
        q = Questions(file_paths)
        q.solution = sol
        print(q.question)
        print(q.submit())


    """
    def __init__(self,fpaths):
        self.question = [Question(fpath) for fpath in fpaths ]


    def solution(self,q):
        """
            Make Own Solution
        """
        return False

    def submit(self):
        result = True
        for i,one_question in enumerate(self.question,1):
            print(f"#{i}")

            real_ans = one_question.answer
            given_ans = self.solution(one_question)
            
            print("Given : \n", given_ans , "\nAnswer : \n", real_ans)
            if given_ans != real_ans:
                result = False
                print(f"#{i} : False\n")
            else:
                print(f"#{i} : True\n")
        return f"Result : {result}"


    def __str__(self):
        return "Questions"

if __name__ == "__main__":

    file_paths = ["ex1.txt" , "ex2.txt"]

    def sol(line):
        print("input:",line.input())
        print("input:",line.input())
        return 3
    # help(Question)
    
    q = Questions(file_paths)
    q.solution = sol
    print(q.question)
    print(q.submit())
