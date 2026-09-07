class Solution:
    def splitListToParts(self, head, k):
        # Step 1: Find length
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        # Step 2: Find size of each part
        part_size = length // k
        extra = length % k

        result = []
        current = head

        # Step 3: Create k parts
        for i in range(k):

            # First 'extra' parts get one extra node
            size = part_size

            if i < extra:
                size += 1

            # Empty part
            if size == 0:
                result.append(None)
                continue

            # Head of current part
            part_head = current

            # Move to the last node of this part
            for j in range(size - 1):
                current = current.next

            # Save beginning of next part
            next_part = current.next

            # Break the current part
            current.next = None

            # Store this part
            result.append(part_head)

            # Move to next part
            current = next_part

        return result