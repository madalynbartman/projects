import time
import rtmidi

out = rtm.MidiOut() #type: ignore

# Making a dictionary so I can refer to the device by name
ports_dict = {k: v for (v,k) in enumerate(out.get_ports())}
out.open_port(ports_dict["OP-Z 1"])

with out:
    note_on = [0x94, 48, 112]
    note_off = [0x84, 48, 0]

    # Set the filter to 0
    cc_msg = [0x84, 3, 0]
    out.send_message(cc_msg)
    time.sleep(0,1)

    # Set note on 
    out.send_message(note_on)
    time.sleep(1)
               
    # Start ramping filter  
    for cc in range(127):
        # 0xB_ is controller change 
        cc_msg = [0x84, 3, cc]
        out.send_message(cc_msg)
        time.sleep(0.1)
    out.send_message(note_off)
    time.sleep(0.1)
