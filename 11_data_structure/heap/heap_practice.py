# 배열을 활용한 heap 구현 예시
class Heap:
    def __init__(self, s_min_max = 'min'):
        self.dynamic_arr = [None, ]
        self.num_of_data = 0

        if s_min_max == 'max':
            self.min_max = 2
        else:
            self.min_max = 1

    def get_parent_idx(self, idx):
        return idx // 2

    def get_left_child_idx(self, idx):
        return idx * 2

    def get_right_child_idx(self, idx):
        return idx * 2 + 1

    def get_prior(self, val1, val2):
        '''
        val1 의 우선순위가 높으면 -1
        val2 의 우선순위가 높으면 1
        우선순위가 같다면 0
        '''

        if self.min_max == 1: # 최소힙
            if val1 < val2:
                return -1
            if val1 > val2:
                return 1
            else:
                return 0
        else: #최대힙(self.min_max == 2)
            if val1 > val2:
                return -1
            if val1 < val2:
                return 1
            else:
                return 0

    def is_empty(self):
        if self.num_of_data == 0:
            return True

        return False

    def size(self):
        return self.num_of_data

    def is_go_up(self, idx, data):
        if idx <= 1:
            return False

        parent_value = self.dynamic_arr[self.get_parent_idx(idx)]

        if self.get_prior(parent_value, data) == 1:
            return True
        else:
            return False

    def insert(self, data):
        if self.is_empty():
            self.dynamic_arr.append(data)
            self.num_of_data += 1
            return

        self.dynamic_arr.append(data)
        self.num_of_data += 1

        idx_data = self.num_of_data

        while self.is_go_up(idx_data, data):
            parent_idx = self.get_parent_idx(idx_data)
            self.dynamic_arr[idx_data] = self.dynamic_arr[parent_idx]

            idx_data = parent_idx

        self.dynamic_arr[idx_data] = data

    def which_is_prior_child(self, idx):
        left_idx = self.get_left_child_idx(idx)
        right_idx = self.get_right_child_idx(idx)
        left_value = self.dynamic_arr[left_idx]
        right_value = self.dynamic_arr[right_idx]

        if left_idx > self.num_of_data:
            return None
        elif left_idx == self.num_of_data:
            return left_idx

        if self.get_prior(left_value, right_value) == -1:
            return left_value
        else:
            return right_value

    def is_go_down(self, idx, data):
        child_idx = self.which_is_prior_child(idx)

        if not child_idx:
            return False

        child_value = self.dynamic_arr[child_idx]

        if self.get_prior(child_value, data) == -1:
            return True
        else:
            return False

    def delete(self):
        if self.is_empty():
            return None

        ret_data = self.dynamic_arr[1]
        last_data = self.dynamic_arr[self.num_of_data]
        self.num_of_data -= 1

        idx_data = 1

        while self.is_go_down(idx_data, last_data):
            child_idx = self.which_is_prior_child(idx_data)
            self.dynamic_arr[idx_data] = self.dynamic_arr[child_idx]
            idx_data = child_idx

        self.dynamic_arr[idx_data] = last_data
        self.dynamic_arr.pop()

        return ret_data


if __name__ == "__main__":
    heap = Heap("min")
    heap.insert(3)
    heap.insert(5)
    heap.insert(1)
    heap.insert(10)
    heap.insert(8)
    heap.insert(7)
    heap.insert(4)
    heap.insert(5)
    heap.insert(2)
    heap.insert(6)
    heap.insert(9)

    for i in range(1, heap.size()+1):
        print(heap.dynamic_arr[i], end = '  ')

    print("\n")

    for i in range(1, heap.size()+1):
        print(heap.delete(), end = '  ')     
