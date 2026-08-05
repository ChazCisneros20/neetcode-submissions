class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        size = len(students)
        i = 0
        while i < size and students:
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
                i = 0 
            else:
                elem = students[0]
                del students[0]
                students.append(elem)
                i+=1

        return len(students)