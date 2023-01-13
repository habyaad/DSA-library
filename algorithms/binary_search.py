### we assume the list is sorted
class BinarySearch:
    def __init__(self) -> None:
        pass
    def search(self, num_list, num)->int:
        i = 0
        j = len(num_list)-1
        while i<=j:
            mid = (i+j)//2
            if i == j:
                return i
            elif num_list[mid] == num:
                return mid
            elif num_list[mid] > num:
                j = mid-1
            elif num_list[mid] < num:
                i = mid+1
            else: 
                return None
if __name__ == "__main__":
    sorted_list = [22,34,45,46,67,97, 177]
    searchAlg = BinarySearch()
    index = searchAlg.search(sorted_list, 97)
    print(index)