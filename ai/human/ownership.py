from collections import deque


class Ownership:
    def __init__(self, groups):
        self.ownerships = []
        self.load_data(groups)

    def load_data(self, groups):
        for group in groups:
            owners = group.owners()
            indexes = [x.id for x in owners]
            self.ownerships.append([group, indexes])
        self.update_data()

    def update_data(self):
        for i, ownership in enumerate(self.ownerships):
            if group.filled():
                owners = group.owners()
                if len(owners) == 1:
                    self.ownerships.pop(i)

    def complete_group(self, ownerships, queue: deque):
        target = queue.pop()
        for i, indexes in enumerate(ownerships):
            queue_copy = queue.copy()
            of_interest = False
            for index in indexes:
                if index != target:
                    queue_copy.append(index)
                else:
                    of_interest = True
            if of_interest:
                ownerships_copy = ownerships.copy()
                ownerships_copy.pop(i)

                self.complete_group()
