# submitted at May 30, 2024 22:49
class Solution:
  def simplifyPath(self, path: str) -> str:
    ans_stack = []
    
    for folder in path.split("/"):
      if folder != "":
        match folder:
          # 因為 "." 是原位置，所以不需要做任何動作 
          case value if value == '..' and len(ans_stack) != 0:
            # ".." 代表要回到上一層，因此要將ans_stack紀錄的路徑去掉最新加入的值
            # 但若一開始就是 "/../" 表示已經在最上層沒辦法再退，因此不需要做任何事情
            ans_stack.pop()
          case value if value not in ["..", "."]:
            # 當遇到非需要特殊處理的狀況一率加入ans_stack
            ans_stack.append(folder)
    # 因為撰寫方式的緣故，會少一開始原目錄的 "/"，因此需要加入
    return "/" + "/".join(ans_stack)