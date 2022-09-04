import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

from datetime import datetime

from prometheus_client import generate_latest

total_list = []
failed_list = []
total_requests = []
success_requests = []
failed_requests = []

time_data = []
success_data = []
failed_data = []
table_data = []

model_banned_counter = 0
model_call_counter = 0


def calculating_metrics(metrics_data):
    """Calculate metrics and call graphs creation."""
    all_metrics = {}

    global time_data
    global table_data
    global success_data
    global failed_data
    global model_call_counter
    global model_banned_counter
    global success_requests
    global total_requests
    global failed_requests

    metric_data = generate_latest()
    try:
        metrics_list = str(metric_data).split('c1_')[1:]
        time_data.append(str(datetime.now().hour))
        for i in metrics_list:
            if '.' in i and '+' not in i:
                name = i.split('{')[0].replace('\n', '')  # 'sasha'
                path = i.split('path="/')[1].split('"')[0]  # '/sasha'
                status = i.split('status="')[1].split('"')[0]  # '200'
                count = i.split(' ')[1].split('.')[0]  # '100'  '1000'

                if len(table_data) == 0:
                    table_data.append(int(count))
                if '23' in time_data:
                    table_data = [int(count) - table_data[0]]

                total_requests.append(int(count))  # [100, 1000]
                if len(total_requests) == 2:
                    total_requests = [total_requests[1] - total_requests[0]]  # [900]

                all_metrics[status] = [name, path, status, total_requests[0]]

                if status == '200':
                    success_requests.append(int(count))  # [100, 1000]
                    if len(success_requests) == 2:
                        success_requests = [success_requests[1] - success_requests[0]]  # [900]
                else:
                    failed_requests.append(int(count))
                    if len(failed_requests) == 2:
                        failed_requests = [failed_requests[1] - failed_requests[0]]

        try:
            percentage_s = success_requests[0] / total_requests[0] * 100  # 100 100
        except (ZeroDivisionError, IndexError):
            percentage_s = 0
        try:
            percentage_f = failed_requests[0] / total_requests[0] * 100  # 0 0
        except (ZeroDivisionError, IndexError):
            percentage_f = 0

        if len(metrics_data) == 0:
            metrics_data.append(all_metrics)  # metrics_data [{'200': ['sasha','/sasha', '200', 100]}]
            try:
                metrics_data.append(success_requests[0])  # [{'200': ['sasha','/sasha', '200', 100]}, 100]
            except IndexError:
                metrics_data.append(0)
            try:
                metrics_data.append(failed_requests[0])
            except IndexError:
                metrics_data.append(0)  # [{'200': ['sasha','/sasha', '200', 100]}, 100, 0]
            metrics_data.append(total_requests[0])  # [{'200': ['sasha','/sasha', '200', 100]}, 100, 0, 100]
            metrics_data.append(percentage_f)  # [{'200': ['sasha','/sasha', '200', 100]}, 100, 0, 100, 0]
            metrics_data.append(percentage_s)  # [{'200': ['sasha','/sasha', '200', 100]}, 100, 0, 100, 0, 100]

        else:
            metrics_data[0] = all_metrics  # {'200': ['sasha','/sasha', '200', 900]}
            metrics_data[1] = success_requests[0]
            metrics_data[2] = failed_requests[0]
            metrics_data[3] = total_requests[0]
            metrics_data[4] = percentage_f
            metrics_data[5] = percentage_s
    except Exception:
        pass
    """Total/Failed graph"""
    if not total_requests and not failed_requests:
        generate_tf_graph(0, 0, '0')

    """Requests line bar"""
    if not failed_requests and not success_requests:
        generate_line_bar(0, 0, '0')
    else:
        try:
            success_data.append(success_requests[0])  # [100]
        except IndexError:
            success_data.append(0)
        try:
            failed_data.append(failed_requests[0])
        except IndexError:
            failed_data.append(0)  # [0]
        generate_line_bar(failed_data, success_data, time_data)
        if '23' in time_data:
            generate_line_bar(failed_data, success_data, time_data)
            generate_tf_graph(model_call_counter, model_banned_counter, time_data)
            success_data.clear()
            table_data.clear()  #
            failed_data.clear()
            time_data.clear()


def generate_tf_graph(success, fail, timing):
    """Model call/no model call"""
    legend = ['Model calls', 'No model calls']
    w = 0.6

    plt.bar(timing, success, w, color='g')
    plt.bar(timing, fail, w, bottom=success, color='b')

    plt.ylabel('Total requests', fontsize=14)
    plt.xlabel('Hour', fontsize=14)
    plt.legend(legend, loc=2)

    plt.savefig('app_gelios/static/total-failed.png')
    plt.close()


def generate_line_bar(fail, success, timing):
    """Requests line bar"""
    legend = ['Success', 'Failed']
    w = 0.6

    plt.bar(timing, success, w, color='g')
    plt.bar(timing, fail, w, bottom=success, color='r')

    plt.ylabel('Total requests', fontsize=14)
    plt.xlabel('Hour', fontsize=14)
    plt.legend(legend, loc=2)

    plt.savefig('app_gelios/static/success-failed.png')
    plt.close()
