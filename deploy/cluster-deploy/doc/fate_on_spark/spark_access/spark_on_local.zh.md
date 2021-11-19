# Spark单机接入FATE指南

## 一. 概述
FATE已经支持spark单机模式

## 二. 部署
需要安装的软件包括: rabbitmq || pulsar(二选一), Nginx

具体部署可参考:
[rabbitmq部署指南](https://github.com/FederatedAI/FATE/blob/master/cluster-deploy/doc/fate_on_spark/rabbitmq_deployment_guide_zh.md)
[pulsar部署指南](https://github.com/FederatedAI/FATE/blob/master/cluster-deploy/doc/fate_on_spark/pulsar_deployment_guide_zh.md).
[Nginx部署指南](https://github.com/FederatedAI/FATE/blob/master/cluster-deploy/doc/fate_on_spark/fate_deployment_step_by_step_zh.md#26-%E9%83%A8%E7%BD%B2nginx)

### 三. 更新FATE配置
### 1.修改default_engines
- "conf/service_conf.yaml"
```yaml
default_engines:
  computing: spark
  federation: rabbitmq
  storage: localfs
```
**注: federation可根据部署情况选择**

### 2.修改rabbitmq或pulsar配置：

**(1)rabbitmq模式**:
- "conf/service_conf.yaml"
```yaml
fate_on_spark
  rabbitmq:
    host: 127.0.0.1
    mng_port: 12345
    port: 5672
    user: fate
    password: fate
    route_table:
  nginx:
    host: 127.0.0.1
    http_port: 9300
    grpc_port: 9310
```
- "conf/rabbitmq_route_table.yaml"
```yaml
10000:
  host: 127.0.0.1
  port: 5672
9999:
  host: 127.0.0.2
  port: 5672
```

**(2)pulsar模式**:
- "conf/service_conf.yaml"
```yaml
fate_on_spark
  pulsar:
    host: 192.168.0.1
    port: 6650
    mng_port: 8080
    topic_ttl: 5
    # default conf/pulsar_route_table.yaml
    route_table:
  nginx:
    host: 127.0.0.1
    http_port: 9300
    grpc_port: 9310
```
- "conf/pulsar_route_table.yaml"
```yaml
9999:
  # host can be a domain like 9999.fate.org
  host: 192.168.0.4
  port: 6650
  sslPort: 6651
  # set proxy address for this pulsar cluster
  proxy: ""

10000:
  # host can be a domain like 10000.fate.org
  host: 192.168.0.3
  port: 6650
  sslPort: 6651
  proxy: ""

default:
  # compose host and proxy for party that does not exist in route table
  # in this example, the host for party 8888 will be 8888.fate.org
  proxy: "proxy.fate.org:443"
  domain: "fate.org"
  port: 6650
  sslPort: 6651
```
### 3. 修改Nginx相关配置
- "conf/service_conf.yaml"
```yaml
fateflow:
  proxy: nginx
fate_on_spark:
  nginx:
    host: 127.0.0.1
    http_port: 9300
    grpc_port: 9310
```

### 4.重启fate flow以使配置生效
```shell script
source /data/projects/fate/bin/init_env.sh
cd /data/projects/fate/fateflow/bin
sh service.sh restart
```

## 四、接入测试
### toy测试
```shell script
source /data/projects/fate/bin/init_env.sh
cd /data/projects/fate/fateflow/
flow test toy --guest-party-id 9999 --host-party-id 10000
```
若出现"success to calculate secure_sum"字样，则说明接入成功

**注意：上面partyid需要填写实际站点id；若没部署fate clinet可通过下面方式离线部署**
- 离线部署fate client

```shell script
source /data/projects/fate/bin/init_env.sh
cd /data/projects/fate/fate/python/fate_client && python setup.py install
```

## 五、使用fate on spark local
### 1. 数据上传

上传引擎使用"localfs", 配置可参考如下:

```json
{
  "file": "examples/data/breast_hetero_guest.csv",
  "id_delimiter": ",",
  "head": 1,
  "partition": 4,
  "namespace": "experiment",
  "table_name": "breast_hetero_guest",
  "storage_engine": "LOCALFS"
}
```
```shell script
cd /data/projects/fate/fateflow/
flow data upload -c examples/upload/upload_to_localfs.json
```

### 2. spark任务提交
- spark的环境:
1. 不部署spark时,系统默认使用pyspark提交spark任务

2. 使用部署的单机版spark时,需要修改fate配置:spark_home:

- conf/service_conf.yaml
```yaml
fate_on_spark:
  spark:
    home: /xxx/xxx
```
系统会使用spark_home提交spark任务
- 使用fate提交任务

使用上述方式在guest方和host方各自上传一份localfs存储类型数据, 并作为reader组件的输入数据发起任务即可