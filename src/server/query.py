from db.DBmanager import base_manager

# type_service statistic
res = base_manager.execute("SELECT COUNT(*) FROM type_service WHERE name='engine repair'")
result_application = res[0]
res = base_manager.execute("SELECT COUNT(*) FROM type_service_statistics WHERE id=1")
result_other = res[0][0] if res and res[0] else 0
if result_other > 0:
    base_manager.execute("""UPDATE type_service_statistics SET engine_repair = ?""", (result_application))
else:
    base_manager.execute("""INSERT INTO type_service_statistics(engine_repair) VALUES(?)""", (result_application))

# application statistics
res = base_manager.execute("SELECT COUNT(*) FROM application WHERE status='done'")
result_application = res[0]
res = base_manager.execute("SELECT COUNT(*) FROM other WHERE id=1")
result_other = res[0][0] if res and res[0] else 0
if result_other > 0:
    base_manager.execute("""UPDATE other SET application = ?""", (result_application))
else:
    base_manager.execute("""INSERT INTO other(application) VALUES(?)""", (result_application))


# sr time(minute) statistics
res = base_manager.execute("""SELECT AVG((strftime('%s', end_time_work) - strftime('%s', start_time_work))/60) AS sr FROM  order_work where id=1;""")
time = res[0]
print(time)
res = base_manager.execute("SELECT COUNT(*) FROM other WHERE id=1")
result_other = res[0][0] if res and res[0] else 0
if result_other > 0:
    base_manager.execute("""UPDATE other SET sr_time_work = ?""", (time))
else:
    base_manager.execute("""INSERT INTO other(sr_time_work) VALUES(?)""", (time))







