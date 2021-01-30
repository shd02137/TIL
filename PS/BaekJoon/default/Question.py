
class Question:
    """ 
        filepath            : file_path
        question_filepath   : sol_file_path
        self.question       : 예제 입력 값
        self.answer         : 예제 정답 값

        How to Use :

        def my_solution():
            answer = "answer"
            return answer 

        q = Question(file_path)
        q.solution = my_solution
        print(q.submit())

    """
    def __init__(self,file_path):
        self.fpath = file_path
        self.question = self.read(self.fpath)
        self.spath = "sol_"+file_path
        self.answer = self.read(self.spath)

    def read(self,fpath):
        lines = ""
        with open(fpath,"r") as f:
            lines = f.read().strip()

        return lines

    def solution(self):
        """
            Make Own Solution
        """
        return False

    def submit(self):
        given_ans = self.solution()
        real_ans = self.answer
        if real_ans.isnumeric():
            real_ans = int(real_ans)
        print("Given : ", given_ans , "Answer : ", real_ans)
        if given_ans == real_ans:
            return True

        return False

if __name__ == "__main__":


    def sol():

        return 3
    # help(Question)
    r = Question("ex1.txt")
    r.solution = sol
    print(r.submit())
