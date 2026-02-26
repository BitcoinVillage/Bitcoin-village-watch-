import hashlib
import json
import time

class BlockchainLogger:
    def __init__(self):
        self.chain = []
        self.pending_logs = []
        
    def hash_block(self, block):
        block_string = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def create_block(self, logs, previous_hash="0"*64):
        block = {
            "timestamp": time.time(),
            "logs": logs,
            "previous_hash": previous_hash
        }
        block["hash"] = self.hash_block(block)
        return block
    
    def add_log(self, log_entry):
        self.pending_logs.append(log_entry)
        
        # Every 3 logs, create a block
        if len(self.pending_logs) >= 3:
            self.mine_block()
    
    def mine_block(self):
        if not self.pending_logs:
            return
        
        previous_hash = self.chain[-1]["hash"] if self.chain else "0"*64
        new_block = self.create_block(self.pending_logs, previous_hash)
        self.chain.append(new_block)
        self.pending_logs = []
        
        return new_block
    
    def log_event(self, event_type, location, data):
        log_entry = {
            "timestamp": time.time(),
            "event_type": event_type,
            "location": location,
            "data": data
        }
        self.add_log(log_entry)
        return log_entry
    
    def verify_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            if current["previous_hash"] != previous["hash"]:
                return False
            
            if current["hash"] != self.hash_block(current):
                return False
        return True

# Test
if __name__ == "__main__":
    logger = BlockchainLogger()
    
    # Simulate events
    logger.log_event("water_quality", "Rampur Village", {"pH": 7.2, "status": "normal"})
    logger.log_event("fund_alert", "Rampur Village", {"amount": 50000, "status": "discrepancy"})
    logger.log_event("water_quality", "Rampur Village", {"pH": 5.8, "status": "alert"})
    
    print("Chain valid:", logger.verify_chain())
    print("Blocks:", len(logger.chain))
    for block in logger.chain:
        print(f"Block {block['hash'][:8]}... → {block['previous_hash'][:8]}...")
