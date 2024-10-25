#!/usr/bin/env bash

fname="fake_output"

prepare_file() {
	# verifica se o named pipe já existe, caso não
	# existir, cria um novo arquivo
	#
	if test -p $fname; then
		return 1
	fi

	mknod -m 660 $fname p
}

random_data() {
	rpm=$(( RANDOM % 3600 ))
	comb=$(( RANDOM % 100 ))
	temp_cvt=$(( RANDOM % 250 ))
	velo=$(( RANDOM % 50 ))

	echo "{\"rpm\": $rpm, \"comb\": $comb, \"temp_cvt\": $temp_cvt, \"velo\": $velo}"
}

prepare_file

# gera o dado aleatório, prepara ele com o jq e joga pro arquivo FIFO
random_data | jq -r > ./$fname
