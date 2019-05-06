# -*-coding:utf-8 -*-
class DijkstraPath():
    def __init__(self, node_map):
        self.node_map = node_map
        self.node_length = len(node_map)
        self.used_node_list = []
        self.collected_node_dict = {}
    def __call__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self._init_dijkstra()
        return self._format_path()
    def _init_dijkstra(self):
        self.used_node_list.append(self.from_node)
        self.collected_node_dict[self.from_node] = [0, -1]
        for index1, node1 in enumerate(self.node_map[self.from_node]):
            if node1:
                self.collected_node_dict[index1] = [node1, self.from_node]
        self._foreach_dijkstra()
    def _foreach_dijkstra(self):
        if len(self.used_node_list) == self.node_length - 1:
            return
        for key, val in self.collected_node_dict.items():  # 遍历已有权值节点
            if key not in self.used_node_list and key != to_node:
                self.used_node_list.append(key)
            else:
                continue
            for index1, node1 in enumerate(self.node_map[key]):  # 对节点进行遍历
                # 如果节点在权值节点中并且权值大于新权值
                if node1 and index1 in self.collected_node_dict and self.collected_node_dict[index1][0] > node1 + val[0]:
                    self.collected_node_dict[index1][0] = node1 + val[0] # 更新权值
                    self.collected_node_dict[index1][1] = key
                elif node1 and index1 not in self.collected_node_dict:
                    self.collected_node_dict[index1] = [node1 + val[0], key]
        self._foreach_dijkstra()
    def _format_path(self):
        node_list = []
        temp_node = self.to_node
        node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        while self.collected_node_dict[temp_node][1] != -1:
            temp_node = self.collected_node_dict[temp_node][1]
            node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        node_list.reverse()
        return node_list
def set_node_map(node_map, node, node_list):
    for x, y, val in node_list:
        node_map[node.index(x)][node.index(y)] = node_map[node.index(y)][node.index(x)] =  val
if __name__ == "__main__":
    node = []
    node_list = [('FloraPrice','E11', 1),('FloraPrice','E9', 1),('FloraPrice','75D}', 1),('NoraFayette','E11', 1),('NoraFayette','E10', 1),('NoraFayette','E13', 1),('NoraFayette','E12', 1),('NoraFayette','E14', 1),('NoraFayette','E9', 1),('NoraFayette','E7', 1),('NoraFayette','E6', 1),('E10','SylviaAvondale', 1),('E10','MyraLiddel', 1),('E10','HelenLloyd', 1),('E10','KatherinaRogers', 1),('VerneSanderson','E7', 1),('VerneSanderson','E12', 1),('VerneSanderson','E9', 1),('VerneSanderson','E8', 1),('E12','HelenLloyd', 1),('E12','KatherinaRogers', 1),('E12','SylviaAvondale', 1),('E12','MyraLiddel', 1),('E14','SylviaAvondale', 1),('E14','75D}', 1),('E14','KatherinaRogers', 1),('FrancesAnderson','E5', 1),('FrancesAnderson','E6', 1),('FrancesAnderson','E8', 1),('FrancesAnderson','E3', 1),('DorothyMurchison','E9', 1),('DorothyMurchison','E8', 1),('EvelynJefferson','E9', 1),('EvelynJefferson','E8', 1),('EvelynJefferson','E5', 1),('EvelynJefferson','E4', 1),('EvelynJefferson','E6', 1),('EvelynJefferson','E1', 1),('EvelynJefferson','E3', 1),('EvelynJefferson','E2', 1),('RuthDeSand','E5', 1),('RuthDeSand','E7', 1),('RuthDeSand','E9', 1),('RuthDeSand','E8', 1),('HelenLloyd','E11', 1),('HelenLloyd','E7', 1),('HelenLloyd','E8', 1),('OliviaCarleton','E11', 1),('OliviaCarleton','E9', 1),('EleanorNye','E5', 1),('EleanorNye','E7', 1),('EleanorNye','E6', 1),('EleanorNye','E8', 1),('E9','TheresaAnderson', 1),('E9','PearlOglethorpe', 1),('E9','KatherinaRogers', 1),('E9','SylviaAvondale', 1),('E9','MyraLiddel', 1),('E8','TheresaAnderson', 1),('E8','PearlOglethorpe', 1),('E8','KatherinaRogers', 1),('E8','SylviaAvondale', 1),('E8','BrendaRogers', 1),('E8','LauraMandeville', 1),('E8','MyraLiddel', 1),('E5','TheresaAnderson', 1),('E5','BrendaRogers', 1),('E5','LauraMandeville', 1),('E5','CharlotteMcDowd', 1),('E4','CharlotteMcDowd', 1),('E4','TheresaAnderson', 1),('E4','BrendaRogers', 1),('E7','TheresaAnderson', 1),('E7','SylviaAvondale', 1),('E7','BrendaRogers', 1),('E7','LauraMandeville', 1),('E7','CharlotteMcDowd', 1),('E6','TheresaAnderson', 1),('E6','PearlOglethorpe', 1),('E6','BrendaRogers', 1),('E6','LauraMandeville', 1),('E1','LauraMandeville', 1),('E1','BrendaRogers', 1),('E3','TheresaAnderson', 1),('E3','BrendaRogers', 1),('E3','LauraMandeville', 1),('E3','CharlotteMcDowd', 1),('E3','flag{', 1),('E2','LauraMandeville', 1),('E2','TheresaAnderson', 1),('KatherinaRogers','E13', 1),('E13','SylviaAvondale', 1)]
    for i in node_list:
        for j in range(2):
            if i[j] in node:
                continue
            else:
                node.append(i[j])
    node_map = [[0 for val in xrange(len(node))] for val in xrange(len(node))]
    set_node_map(node_map, node, node_list)
    # A -->; D
    from_node = node.index('flag{')
    to_node = node.index('75D}')
    dijkstrapath = DijkstraPath(node_map)
    path = dijkstrapath(from_node, to_node)
    for i in path:
        print(node[i[0]])
    print path