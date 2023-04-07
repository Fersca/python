import csv
import json

csvfile = open('/Users/Fernando.Scasserra/Downloads/base_extraction.csv', 'r')
jsonfile = open('example_calls.json', 'w')

fieldnames = ('wmd_id', 'wmd_session_creation_time', 'wmd_channel_name', 'wmd_creation_time', 'wmd_queue', 'wmd_customer_id', 'phone_ten_digits', 'wmd_template', 'wmd_message', 'wmd_image_url', 'wmd_image_caption', 'wmd_audio_url', 'wmd_video_url', 'wmd_file_url', 'wmd_sent_by', 'wmd_msg_from_name', 'wmd_operator_id', 'wmd_operator_email', 'wmd_user_location', 'wmd_creation_time_unix', 'wmd_chat_platform_id', 'wmd_msg_variables', 'wmd_message_has_image', 'wmd_message_has_file', 'wmd_message_has_audio', 'wmd_message_has_video', 'wmd_has_template_condicionado', 'wmd_has_template_approv', 'wmd_has_template_promokcapital', 'wmd_has_template_tiemporeserva', 'wmd_has_template_reactivar_conv', 'wmd_operator_name', 'wmd_operator_role', 'wmd_rule_name', 'wmd_creation_date', 'wmd_process_time')

reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

print("Ready!")