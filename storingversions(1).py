import json
import zlib

class VersionControlSystem:
    def __init__(self, base_version):
        self.base_version = base_version
        self.deltas = []

    def add_version(self, new_version):
        # Calculate delta between new version and the last version
        delta = self.calculate_delta(self.base_version, new_version)
        self.deltas.append(delta)

    def calculate_delta(self, old_version, new_version):
        # Simplified delta calculation 
        # You may need a more complex algorithm for other file types
        return self.compute_changes(old_version, new_version)

    def compute_changes(self, old_version, new_version):
        # Placeholder for computing changes between versions
        # You need to implement this based on your file format
        # Example: For text files, you might use diff algorithms
        # For simplicity, assume new version replaces the old version
        return new_version

    def generate_version(self, version_number):
        # Generate a specific version by applying deltas
        reconstructed_version = self.base_version
        for i in range(version_number):
            reconstructed_version = self.apply_delta(reconstructed_version, self.deltas[i])
        return reconstructed_version

    def apply_delta(self, base_version, delta):
        # Apply delta to base version to get the new version
        # Example: For text files, apply changes to reconstruct the version
        return delta

    def save_to_file(self, file_path):
        # Serialize base version and deltas to a file
        data = {
            'base_version': self.base_version,
            'deltas': self.deltas
        }
        with open(file_path, 'wb') as file:
            serialized_data = zlib.compress(json.dumps(data).encode())
            file.write(serialized_data)

    @classmethod
    def load_from_file(cls, file_path):
        # Load base version and deltas from a file
        with open(file_path, 'rb') as file:
            serialized_data = zlib.decompress(file.read())
            data = json.loads(serialized_data.decode())
            vcs = cls(data['base_version'])
            vcs.deltas = data['deltas']
            return vcs

# Example 
base_version = "Base version of the file"
vcs = VersionControlSystem(base_version)

# Add new versions
new_version1 = "Modified version 1"
vcs.add_version(new_version1)

new_version2 = "Modified version 2"
vcs.add_version(new_version2)

# Save 
vcs.save_to_file("vcs_data.bin")

# Load 
loaded_vcs = VersionControlSystem.load_from_file("vcs_data.bin")

# Generate a specific version
reconstructed_version = loaded_vcs.generate_version(1)
print("Reconstructed Version 1:", reconstructed_version)
