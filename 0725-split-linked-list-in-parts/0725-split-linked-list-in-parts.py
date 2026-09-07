class Solution:
    def splitListToParts(self, head, k):
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        part_size = length // k
        extra = length % k

        result = []
        current = head

        for i in range(k):

            size = part_size

            if i < extra:
                size += 1

            if size == 0:
                result.append(None)
                continue

            part_head = current

            for j in range(size - 1):
                current = current.next

            next_part = current.next

            current.next = None

            result.append(part_head)

            current = next_part

        return result