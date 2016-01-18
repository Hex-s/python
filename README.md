# python

1.变量
  1) a = 1, b = 1 => id(a) == id(b) == id(a) -> true
  2) a = 1,a = '1' 内存地址发生变化
  3) a = [1,2,3], b = [1,2,3] => id(a) == id(b) -> false
  4) a = [1,2,3], b = a => id(a) == id(b) ->true ,b[0] = 0 => a[0] = 0
  5) a = [1,2,3], b = a[0:] => id(a) == id(b) -> false
  
2.strip
  "abc:def:ghi".split(":") => ['abc','def','ghi']

3.strip
  ' a '.strip() => 'a'
  
4.list
  list('abc') => ['a','b','c']
  
5.切片
  a = 'abcdefg'
  a[0] = 'a' ; a[:2] = 'ab' ; a[1:] = 'bcdefg' ; a[1:100] = 'bcdefg' ; a[::2] = 'aceg' 跨步截取 ； a[-4:-1:1] = 'def' ; a[-2:-5:-1] = 'feg' 向后截取
  
