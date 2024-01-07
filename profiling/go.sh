#!/bin/bash

bash ./clean_recoverable.sh
bash ./build_apps.sh
bash ./generate_input_data.sh
bash ./update_data.sh
