A.列表 list
  1.变量
    1) a = 1, b = 1 => id(a) == id(b) == id(a) -> true
    2) a = 1,a = '1' 内存地址发生变化
    3) a = [1,2,3], b = [1,2,3] => id(a) == id(b) -> false
    4) a = [1,2,3], b = a => id(a) == id(b) ->true ,b[0] = 0 => a[0] = 0
    5) a = [1,2,3], b = a[0:] => id(a) == id(b) -> false
    
    6) s1 = '12', s2 = '12' => id(s1) == id(s2) -> true
    7) s1 = '12', s2 = s1 , s1 = '21' -> s1 = '12', s2 = '21'
  
  2.split
    "abc:def:ghi".split(":") => ['abc','def','ghi']

  3.strip
    ' a '.strip() => 'a'
  
  4.list
    list('abc') => ['a','b','c']
  
  5.切片
    a = 'abcdefg'
    a[0] = 'a' ; a[:2] = 'ab' ; a[1:] = 'bcdefg' ; a[1:100] = 'bcdefg' ; a[::2] = 'aceg' 跨步截取 ； a[-4:-1:1] = 'def' ; a[-2:-5:-1] = 'feg' 向后截取
  
  
  6.方法 a = [1,2,3],b = [4]
    1)  a.append(4), a = [1,2,3,4]
    2)  a.count(3) -> 1
    3)  a.extend(b), a = [1,2,3,4]
    4)  a.insert(0,2),(location,value) a = [2,1,2,3]
    5)  a.pop(), a = [1,2] 删除最后一个,返回最后一个被删除的序列下标
    6)  del(a[0]), a = [2,3]
    7)  a = [2,2,2], a.remove(2), a = [2,2] 删除第一个出现的元素
    8)  a.reverse(), a = [3,2,1] 本身发生变化
    9)  a.sort(), a = [1,2,3] 本身发生变化
    10）c = list(reversed(a)) 本身不发生变化
    11) max(a) = 3
    12) min(a) = 1
    13) sum(a) = 6
    14) range(1,101) [1,....,100]
    15) import random random.shuffle(a) 打乱a的顺序
    16) random.randrange(1,101) 1-100间的随机数
    17) a = ['1','2'] , b = ('/').join(a) = '1/2',b.split('/') = ['1','2']  字符串的分割
    
B.元组 tuple a = (1,2,3) 元组不可改变
  1. a.append(4) X没有append,数据只供查询不可改变
  2. b = list(a) = [1,2,3]
  3. (a,b,c) = (1,2,3)
      a => 1
      a,b,c => (1,2,3)
      d = a,b,c => (1,2,3)
      a,b = b,a  => a=2,b=1
  4. a = (1),type(a) = int ; a = (1,) , type(a) = tuple
  5. a.count(1) = 1

C.字符串 string s = '123'
  1. max(s) = 3 , min(str) = 1
  2. s*2 = '123123'
  3. string s = 'abc'
     s.capitalize() 首字母大写 'Abc'
  4. s.replace('1','X') 'X23
  
D.字典 python中唯一的映射类型
  1. a = [ (1,1),(2,2),(3,3) ] , b = [1,2,3] , dict(zip(b,a)) = {1:(1,1),2:(2,2),3:(3,3)}
  2. a = [ [1,1],[2,2] ] , dict(a) = {1:1,2:2}
  3. a = {1:'1',2:'2'}
      for k in a:print(k) 1 2
      for k in a:print(a[k]) '1' '2'
      for k,v in a.items():print(k,v) 1 '1'   2 '2'
  4. 方法 a = {1:'a',2:'b',3:'c'}
      1) del(a[1]) , a = {2:'b',3:'c'}  ;  del a[1]  , {2:'b',3:'c'}  ;  a.pop(3) , {1:'a',2:'b'}  ;  del(a)  , a不存在了
      2) a.clear()  , a = {}
      3) a.get(1,'error')
      4) a.update({4:'d'}) 连接两个字典，key重复则覆盖
      5) a.keys()  -> dict_keys([1, 2, 3])  ; a.values()  -> dict_values(['a', 'b', 'c'])  type不是list，但是可以循环
      6) a.setdefault(4,'d')  存在a[4]则返回a[4]，否则添加新键，值为'd'
      5) a.pop('4','error')  有a[4]则删除，没有则返回error
      6) a.items() -> [(1,'a'),(2,'b'),(3,'c')] 返回键值对元组的列表
  5.  构建字典
      a = [1,2,3]  b = ['a'.'b','c']
      c = zip(a,b) -> [(1,'a'),(2,'b'),(3,'c')]
      d = dict(c) -> {1:'a',2:'b',3:'c'}
      d = dict(zip(a,b))
  6. 序列不能作为键
  
E: set 
  1. a = {1,1,2,3} , a = {1,2,3}
  2. a = {1,2,3} , a.add(3) -> {1,2,3}  , a.add(4)  -> {1,2,3,4}
  3. a.pop() -> a = {2,3} 删除头一个  ;   a.remove(2) = {1,3}
  4. a = {1,2,3},  b = {2,3,4}  交集:a&b = {2,3}  并集: a|b = {1,2,3,4}
  
F: 排序 判断
  1.  a = [ [1,3],[2,2],[3,1] ]
      1)  b = sorted(a) -> b = [ [1,3],[2,2],[3,1] ]
      1)  def sort_by_key(n):
            return n[1]
          b = sorted(a,key=sort_by_key)
      2)  b = sorted(a,key=lambda x:x[1])  -> b = [ [3,1],[2,2],[1,3] ]
  
  2.a = [ [1,3,5],[2,4,4],[4,5,3],[1,4,5] ] 
    1)  b = sorted(a) -> b = [ [1,3,5],[1,4,5],[2,4,4],[4,5,3] ]
    2)  b = sorted(a,key=lambda n:(n[1],n[2])) -> b = [ [1,3,5],[2,4,4],[1,4,5],[4,5,3] ]
    3)  def sort_by_k1_k2(n):
          return (n[1],n[2])
        b = sorted(a,key=sort_by_k1_k2)
        
G: lambda,map
    a = [ [1,3,5],[2,4,4],[4,5,3],[1,4,5] ] 
    b = list(map(len,a))  -> b=[3,3,3,3]
