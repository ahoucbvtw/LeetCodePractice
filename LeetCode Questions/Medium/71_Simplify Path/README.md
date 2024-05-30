# LeetCode 71 Simplify Path
Given an absolute path for a Unix-style file system, which begins with a slash `'/'`, transform this path into its **simplified canonical path**.

In Unix-style file system context, a single period `'.'` signifies the current directory, a double period `".."` denotes moving up one directory level, and multiple slashes such as `"//"` are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like `"..."`) as valid names for files or directories.

The simplified canonical path should adhere to the following rules:

- It must start with a single slash `'/'`.
- Directories within the path should be separated by only one slash `'/'`.
- It should not end with a slash `'/'`, unless it's the root directory.
- It should exclude any single or double periods used to denote current or parent directories.

Return the new path.

Example 1:
```
Input: path = "/home/"
Output: "/home"

Explanation:
The trailing slash should be removed.
```

Example 2:
```
Input: path = "/home//foo/"
Output: "/home/foo"

Explanation:
Multiple consecutive slashes are replaced by a single one.
```

Example 3:
```
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"

Explanation:
A double period ".." refers to the directory up a level.
```

Example 4:
```
Input: path = "/../"
Output: "/"

Explanation:
Going one level up from the root directory is not possible.
```

Example 5:
```
Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"

Explanation:
"..." is a valid name for a directory in this problem.
```

Constraints:

- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, period `'.'`, slash `'/'` or `'_'`.
- `path` is a valid absolute Unix path.

## Topic
- Stack
- String

## My Thinking
題目要將 `Input path` 改成 `simplified canonical path`。
因此就必須要知道一些規則：
- 必須以單一斜線開頭 `'/'`。
- 路徑中的目錄應僅以一個斜線分隔 `'/'`。
- 它不應該以斜線結尾 `'/'`，除非它是 `根目錄`。
- 排除 `.` , `..`。因為 `.` 代表當前目錄，`..` 代表當前目錄的 `父目錄` => `上一層目錄`。

在了解上述規則後，尤其是第4點非常重要，因為會需要做路徑上的操作。
因此題的解題思路：
- 因為是要做 `path`，所以利用 `Stack` 資料結構特性，啟用一陣列變數。
- 當遇到 `.` 時不需要做任何操作，因為它代表當前目錄，另外也不能把它放進陣列中。
- 當遇到 `..` 時需要回到上一層，因為它代表當前目錄的 `父目錄` => `上一層目錄`，另外也不能把它放進陣列中。<br>而回到上一層的操作只需要對 `Stack` 陣列進行 `pop()`，就可以讓在最底層目錄回到上一層。
- 當不是遇到 `.` 和 `..` 時都需要加入到 `Stack` 陣列中，因為並非特殊條件。
- 最後因為撰寫方式的緣故，需要在 `output` 加入 `"/"` 為開頭。<br>連 `/../`, `/./` 也一樣最後都會需要轉換後變成 `'/'`。

### Complexity
Time complexity: O(n)
> 因為先對字串使用 `split()` 後，再使用迴圈遍歷查詢字串，因此為 **O(n)**

Space complexity: O(n)
> 因為在迴圈遍歷確認過程中使用 `Stack` 陣列去紀錄，因此為 **O(n)**。