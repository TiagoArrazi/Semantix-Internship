from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'semantix'
app.config['MYSQL_DB'] = 'alunosDB'

mysql = MySQL(app)

alarm_1 = {"@version": "1", "nbiClearUser": "11164043", "nbiSpecificProblem": "7407|PORTA ABERTA GAB SERVICO",
           "@timestamp": "2018-12-18T17:54:59.989Z", "nbiObjectInstance": "PLMN-PLMN/BSC-220683/BCF-158",
           "type": "snmp", "nbiAlarmTime": "2018-12-18,15:54:46.0,-2:0", "nbiAlarmId": "65182239",
           "SNMPv2-MIB::snmpTrapOID.0": "SNMPv2-SMI::enterprises.28458.1.26.3.0.1.1",
           "nbiEventTime": "2018-12-18,15:54:59.5,-2:0", "nbiPerceivedSeverity": "1",
           "nbiAdditionalText": "|EXTERNAL AL 7|FF FF FF FF FF FF||||", "nbiAlarmType": "5", "nbiProbableCause": "0",
           "host": "10.119.218.142",
           "message": "#<SNMP::SNMPv2_Trap:0x35cd1e5e @request_id=1679369471, @error_index=0, @error_status=0, @source_ip=\"10.119.218.142\", @varbind_list=[#<SNMP::VarBind:0x696c7869 @name=[1.3.6.1.2.1.1.3.0], @value=#<SNMP::TimeTicks:0x6c47bd31 @value=475081494>>, #<SNMP::VarBind:0x31a57109 @name=[1.3.6.1.6.3.1.1.4.1.0], @value=[1.3.6.1.4.1.28458.1.26.3.0.1.1]>, #<SNMP::VarBind:0x58412f07 @name=[1.3.6.1.4.1.28458.1.26.2.1.3.9], @value=#<SNMP::Integer:0x93eaf0b @value=11164043>>, #<SNMP::VarBind:0x1309ba1c @name=[1.3.6.1.4.1.28458.1.26.3.1.1.5], @value=\"65182239\">, #<SNMP::VarBind:0x64ca2645 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.7], @value=#<SNMP::Integer:0x352204cc @value=5>>, #<SNMP::VarBind:0x4998a394 @name=[1.3.6.1.4.1.28458.1.26.2.1.6.5], @value=\"PLMN-PLMN/BSC-220683/BCF-158\">, #<SNMP::VarBind:0x171f29e1 @name=[1.3.6.1.4.1.28458.1.26.2.1.6.3], @value=\"2018-12-18,15:54:59.5,-2:0\">, #<SNMP::VarBind:0x22d2dd49 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.6], @value=\"2018-12-18,15:54:46.0,-2:0\">, #<SNMP::VarBind:0x773b9bb @name=[1.3.6.1.4.1.28458.1.26.3.1.1.14], @value=#<SNMP::Integer:0xb7b2ec2 @value=0>>, #<SNMP::VarBind:0x65c55e6d @name=[1.3.6.1.4.1.28458.1.26.3.1.1.16], @value=\"7407|PORTA ABERTA GAB SERVICO\">, #<SNMP::VarBind:0x5149ef09 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.13], @value=#<SNMP::Integer:0x4bed3afa @value=1>>, #<SNMP::VarBind:0x1932007b @name=[1.3.6.1.4.1.28458.1.26.3.1.1.15], @value=\"\">, #<SNMP::VarBind:0x56cb1306 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.4], @value=\"|EXTERNAL AL 7|FF FF FF FF FF FF||||\">, #<SNMP::VarBind:0x48e48f71 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.19], @value=\"NEName=PIISL01|controlObjName=BSCPI35\">]>",
           "nbiProposedRepairAction": "", "sysUpTime": "54 days, 23:40:14.94",
           "nbiOptionalInformation": "NEName=PIISL01|controlObjName=BSCPI35"}

alarm_2 = {"@version": "1", "nbiClearUser": "11164202", "nbiSpecificProblem": "7406",
           "@timestamp": "2018-12-18T17:57:08.422Z", "nbiObjectInstance": "PLMN-PLMN/BSC-211069/BCF-137",
           "type": "snmp", "nbiAlarmTime": "2018-12-18,15:56:53.0,-2:0", "nbiAlarmId": "65182326",
           "SNMPv2-MIB::snmpTrapOID.0": "SNMPv2-SMI::enterprises.28458.1.26.3.0.1.1",
           "nbiEventTime": "2018-12-18,15:57:8.2,-2:0", "nbiPerceivedSeverity": "2",
           "nbiAdditionalText": "|EXTERNAL AL 6|FF FF FF FF FF FF||||", "nbiAlarmType": "5", "nbiProbableCause": "0",
           "host": "10.119.218.142",
           "message": "#<SNMP::SNMPv2_Trap:0x5cc713fd @request_id=1679369630, @error_index=0, @error_status=0, @source_ip=\"10.119.218.142\", @varbind_list=[#<SNMP::VarBind:0xc861bb9 @name=[1.3.6.1.2.1.1.3.0], @value=#<SNMP::TimeTicks:0x31eebb21 @value=475094369>>, #<SNMP::VarBind:0x55d21e1a @name=[1.3.6.1.6.3.1.1.4.1.0], @value=[1.3.6.1.4.1.28458.1.26.3.0.1.1]>, #<SNMP::VarBind:0x63a5ded7 @name=[1.3.6.1.4.1.28458.1.26.2.1.3.9], @value=#<SNMP::Integer:0x5fc24ac9 @value=11164202>>, #<SNMP::VarBind:0x1bb1d5a3 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.5], @value=\"65182326\">, #<SNMP::VarBind:0x5e562a01 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.7], @value=#<SNMP::Integer:0x13c8147a @value=5>>, #<SNMP::VarBind:0x5e9190c8 @name=[1.3.6.1.4.1.28458.1.26.2.1.6.5], @value=\"PLMN-PLMN/BSC-211069/BCF-137\">, #<SNMP::VarBind:0x4b984a74 @name=[1.3.6.1.4.1.28458.1.26.2.1.6.3], @value=\"2018-12-18,15:57:8.2,-2:0\">, #<SNMP::VarBind:0x24716724 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.6], @value=\"2018-12-18,15:56:53.0,-2:0\">, #<SNMP::VarBind:0x77c9dc14 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.14], @value=#<SNMP::Integer:0x250c15f5 @value=0>>, #<SNMP::VarBind:0x2c4e20ca @name=[1.3.6.1.4.1.28458.1.26.3.1.1.16], @value=\"7406\">, #<SNMP::VarBind:0x3292a20 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.13], @value=#<SNMP::Integer:0x3a397f2d @value=2>>, #<SNMP::VarBind:0x7f5f6622 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.15], @value=\"\">, #<SNMP::VarBind:0x224a4173 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.4], @value=\"|EXTERNAL AL 6|FF FF FF FF FF FF||||\">, #<SNMP::VarBind:0x68780730 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.19], @value=\"NEName=PASBJ02|controlObjName=BSCPA04\">]>",
           "nbiProposedRepairAction": "", "sysUpTime": "54 days, 23:42:23.69",
           "nbiOptionalInformation": "NEName=PASBJ02|controlObjName=BSCPA04"}

alarm_5 = {"@version": "1", "nbiClearUser": "NE", "nbiSpecificProblem": "8099",
           "@timestamp": "2018-12-18T17:54:59.945Z",
           "nbiObjectInstance": "PLMN-PLMN/BSC-218437/BCF-756/TRE-1/FUE-1/SB-2", "nbiClearSystemId": "NE",
           "type": "snmp", "nbiAlarmId": "65182218",
           "SNMPv2-MIB::snmpTrapOID.0": "SNMPv2-SMI::enterprises.28458.1.26.3.0.1.5",
           "nbiEventTime": "2018-12-18,15:54:59.3,-2:0", "nbiClearTime": "2018-12-18,15:54:48.0,-2:0",
           "nbiPerceivedSeverity": "5",
           "nbiAdditionalText": "02 4080d 01 2d|UltraSiteBTSHub      FXC E1/T1 Symm       E1/T1 IF2|FF FF FF FF FF FF||||",
           "nbiAlarmType": "1", "nbiProbableCause": "0", "host": "10.119.218.142",
           "message": "#<SNMP::SNMPv2_Trap:0x4951b551 @request_id=1679369468, @error_index=0, @error_status=0, @source_ip=\"10.119.218.142\", @varbind_list=[#<SNMP::VarBind:0x6f7d7083 @name=[1.3.6.1.2.1.1.3.0], @value=#<SNMP::TimeTicks:0x38ca7947 @value=475081476>>, #<SNMP::VarBind:0x7cf5a832 @name=[1.3.6.1.6.3.1.1.4.1.0], @value=[1.3.6.1.4.1.28458.1.26.3.0.1.5]>, #<SNMP::VarBind:0x35d9b847 @name=[1.3.6.1.4.1.28458.1.26.2.1.3.9], @value=#<SNMP::Integer:0x31a42f17 @value=11164040>>, #<SNMP::VarBind:0x5a4f7825 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.5], @value=\"65182218\">, #<SNMP::VarBind:0xb2aff66 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.7], @value=#<SNMP::Integer:0x73c975c4 @value=1>>, #<SNMP::VarBind:0x6385303d @name=[1.3.6.1.4.1.28458.1.26.2.1.6.5], @value=\"PLMN-PLMN/BSC-218437/BCF-756/TRE-1/FUE-1/SB-2\">, #<SNMP::VarBind:0x422af238 @name=[1.3.6.1.4.1.28458.1.26.2.1.6.3], @value=\"2018-12-18,15:54:59.3,-2:0\">, #<SNMP::VarBind:0x1e27f4d4 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.14], @value=#<SNMP::Integer:0x2678c581 @value=0>>, #<SNMP::VarBind:0x6cb61dab @name=[1.3.6.1.4.1.28458.1.26.3.1.1.16], @value=\"8099\">, #<SNMP::VarBind:0x79988937 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.13], @value=#<SNMP::Integer:0x58385384 @value=5>>, #<SNMP::VarBind:0x388cc1cf @name=[1.3.6.1.4.1.28458.1.26.3.1.1.4], @value=\"02 4080d 01 2d|UltraSiteBTSHub      FXC E1/T1 Symm       E1/T1 IF2|FF FF FF FF FF FF||||\">, #<SNMP::VarBind:0x648bc830 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.18], @value=\"NE\">, #<SNMP::VarBind:0x59e734a7 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.8], @value=\"2018-12-18,15:54:48.0,-2:0\">, #<SNMP::VarBind:0x43d9e86c @name=[1.3.6.1.4.1.28458.1.26.3.1.1.9], @value=\"NE\">, #<SNMP::VarBind:0x1d85cb61 @name=[1.3.6.1.4.1.28458.1.26.3.1.1.19], @value=\"NEName=|controlObjName=BSCCE38\">]>",
           "sysUpTime": "54 days, 23:40:14.76", "nbiOptionalInformation": "NEName=|controlObjName=BSCCE38"}


@app.route('/alunos', methods=['GET'])
def get_all():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM alunos')
    return jsonify(cursor.fetchall())


@app.route('/alunos/<int:student_id>', methods=['GET'])
def by_id(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM alunos WHERE id={}'.format(student_id))
    return jsonify(cursor.fetchall())


@app.route('/alunos/<string:student_name>', methods=['GET'])
def by_name(student_name):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM alunos WHERE nome LIKE "%{}%"'.format(student_name))
    return jsonify(cursor.fetchall())


@app.route('/alarmes/1', methods=['GET'])
def get_alarm_1():
    return jsonify(alarm_1)


@app.route('/alarmes/2', methods=['GET'])
def get_alarm_2():
    return jsonify(alarm_2)


@app.route('/alarmes/5', methods=['GET'])
def get_alarm_5():
    return jsonify(alarm_5)


if __name__ == '__main__':
    app.run(port=80, debug=True)
