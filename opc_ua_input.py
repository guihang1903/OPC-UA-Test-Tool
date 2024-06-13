from opcua import Client

class OPCUATestTool:
    def __init__(self, server_url):
        self.server_url = server_url
        self.client = Client(server_url)

    def connect(self):
        try:
            self.client.connect()
            print(f"Connected to OPC UA server at {self.server_url}")
        except Exception as e:
            print(f"Failed to connect to OPC UA server: {e}")

    def browse_and_print(self, node, level=0):
        try:
            children = node.get_children()
            for child in children:
                indent = "  " * level
                browse_name = child.get_browse_name()
                node_id = child.nodeid
                print(f"{indent}Node: {node_id}, BrowseName: {browse_name}")
                self.browse_and_print(child, level + 1)
        except Exception as e:
            print(f"Failed to browse node: {e}")

    def read_node_value(self, node_id):
        try:
            node = self.client.get_node(node_id)
            value = node.get_value()
            print(f"Value of node {node_id}: {value}")
        except Exception as e:
            print(f"Failed to read node value: {e}")

    def disconnect(self):
        self.client.disconnect()
        print("Disconnected from OPC UA server")

if __name__ == "__main__":
    print("OPC UA Test Tool")
    print("Author: Yuan Peng")  # Replace "Your Name" with your actual name
    print("Date: 2024/06/13")
    print("====================")

    server_url = input("Enter the OPC UA server URL (e.g., opc.tcp://localhost:4840): ")
    opcua_test_tool = OPCUATestTool(server_url)
    opcua_test_tool.connect()

    # Start browsing from the root node
    root_node = opcua_test_tool.client.get_root_node()
    print("Browsing the OPC UA server:")
    opcua_test_tool.browse_and_print(root_node)

    while True:
        node_id = input("Enter the node ID you want to read (e.g., ns=2;i=2) or type 'exit' to quit: ")
        if node_id.lower() == 'exit':
            break
        opcua_test_tool.read_node_value(node_id)

    opcua_test_tool.disconnect()
    print("Program exited. Press any key to close...")
    input()
