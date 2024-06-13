from opcua import Client

class OPCUATestTool:
    def __init__(self, server_url):
        self.server_url = server_url
        self.client = Client(server_url)

    def connect(self):
        try:
            self.client.connect()
            print(f"Connected to OPC UA server") # at {self.server_url}
        except Exception as e:
            print(f"Failed to connect to OPC UA server: {e}")

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
    # 替换 'opc.tcp://localhost:4840' 使用您的OPC UA服务器URL
    server_url = 'opc.tcp://10.82.51.10:4840'
    node_id = 'ns=4;s=.PDC_Read.actual.cycleStart'  # 替换为要读取的节点ID
    #node_id = 'ns=4;s=.PDC_Read.partProgram.filename' 
    #node_id = 'ns=4;s=.PDC_Read.actual.elapsedTime' 
    #node_id = 'ns=4;s=.PDC_Read.actual.cycleStart'
    opcua_test_tool = OPCUATestTool(server_url)
    opcua_test_tool.connect()
    opcua_test_tool.read_node_value(node_id)
    opcua_test_tool.disconnect()



# 个脚本包含一个 OPCUATestTool 类，该类封装了与 OPC UA 服务器的连接、读取节点值和断开连接的功能。你可以根据自己的需求修改 server_url 和 node_id。

# 以下是脚本的工作流程：
# 创建 OPCUATestTool 对象并传入 OPC UA 服务器的 URL。
# 调用 connect 方法连接到服务器。
# 使用 read_node_value 方法读取指定节点的值。
# 调用 disconnect 方法断开与服务器的连接。
# 确保在运行脚本之前，根据你的 OPC UA 服务器配置，替换正确的 server_url 和 node_id。