import boto3


def update_node_group_size(cluster_name, node_group_name, size):
    eks_client = boto3.client('eks')
    try:
        # 노드 그룹 크기 업데이트
        response = eks_client.update_nodegroup_config(
            clusterName=cluster_name,
            nodegroupName=node_group_name,
            scalingConfig={
                'minSize': size,
                'maxSize': size+1,
                'desiredSize': size
            }
        )
        print(f"Successfully updated node group '{node_group_name}' in cluster '{cluster_name}' to size {size}")
        return response
    except Exception as e:
        print(f"Error updating node group size: {e}")
        raise


def lambda_handler(event, context):
    # 설정: 클러스터 이름, 노드 그룹 이름, 크기
    cluster_name = '클러스터이름'  # 클러스터 이름을 입력하세요
    node_group_name = '노드그룹이름'  # 노드 그룹 이름을 입력하세요
    size = 0  # 최소, 최대, 원하는 크기를 모두 0로 설정 (desired 값)
    update_node_group_size(cluster_name, node_group_name, size)
