import time
class Database:
    def __init__(self):
        self.query_count = 0
        self.data = {i: f"Detail {i}" for i in range(100)}
    def query(self, item_id):
        self.query_count += 1
        time.sleep(0.01)
        return self.data.get(item_id)
    def query_multiple(self, item_ids):
        self.query_count += 1
        time.sleep(0.01)
        return {item_id: self.data.get(item_id) for item_id in item_ids}
def process(details):
    pass
db = Database()
items = [type('Item', (), {'id': i}) for i in range(50)]

# Use eager loading / batch querying to fix the N+1 issue
item_ids = [item.id for item in items]
all_details = db.query_multiple(item_ids)
for item in items:
    details = all_details.get(item.id)
    process(details)

if __name__ == "__main__":
    print(f"Total queries: {db.query_count}")
