"""
Problem Statement:
------------------
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). 
Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note: We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. 
The input format you see is mainly to ensure our tests' comprehensiveness.

Example 1:
Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). 
"firstsecondthird" is the correct output.

Example 2:
Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
"""

# Link --> https://leetcode.com/problems/print-in-order/

# Code:
import threading
class Foo:
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    def __init__(self):
        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst: 'Callable[[], None]'):
        printFirst()
        self.lock1.release()


    def second(self, printSecond: 'Callable[[], None]'):
        self.lock1.acquire()
        printSecond()
        self.lock1.release()
        self.lock2.release()


    def third(self, printThird: 'Callable[[], None]'):
        self.lock2.acquire()
        printThird()
        self.lock2.release()
