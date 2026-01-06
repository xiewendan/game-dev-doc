default:
        just help

set positional-arguments
@switch jdir jbranch:
        #!/bin/bash
        echo $@
        if [ "{{jdir}}" = "test" ]; then
                sbranch="trunk"
        else
                sbranch="{{jbranch}}"
        fi
        cd /home/xxx/project/{{jdir}}/aaa && svn switch svn:///$sbranch

@update *args='':
        cd /home/xxx/project/$1/aaa && svn up --ignore-externals
        cd /home/xxx/project/$1/aaa && svn up -r $2 aa

@build *args='':
        cd /home/xxx/project/$1/aaa/ && sh build.sh

@start jdir:
        #!/bin/bash
        case "{{jdir}}" in
                        "test")           sconfig="config.8790" ;;
                        "trunk")          sconfig="config.7492" ;;
                        *)                sconfig="" ;;
        esac 

        cd /home/xxx/project/{{jdir}} && aaa -C $sconfig

stop:
        ps -aux | grep -e "key1" -e key2 | awk '{print $2}' | xargs kill -9

@log *args='':
        tmux send-keys "cd /home/xxx/project/$1/aaa/log" Enter

@tailf *args='':
        #!/bin/bash
        cd /home/xxx/project/$1
        shift
        iname=$1
        shift
        patterns=$@
        echo "xxxtodo $patterns"
        cmd="find path1 path2 -iname $iname | xargs tail -f"
        if [ -z "$patterns" ]; then
                echo "eval $cmd"
                eval "$cmd"
        else
                for pattern in $patterns; do
                        cmd="$cmd | grep --color=always --line-buffered '$pattern'"
                done
                echo "eval $cmd"
                eval "$cmd"
        fi

@diff file1 file2:
        #!/bin/bash
        cd {{invocation_directory()}}
        vimdiff {{file1}} {{file2}}

help:
        @echo ""
        @echo "shuoming:  dir in the command is xinshou|test|trunk" 
        @echo ""
        @echo "all the self define command"
        @echo "  switch -- switch dir branch   -- just switch xinshou branches/xxx_hdnpc"
        @echo "  update -- update dir svn_version   -- just update xinshou 2282121"
        @echo "  build -- build dir  -- just build xinshou"
        @echo "  start -- start dir -- just start xinshou"
        @echo "  stop -- stop the server -- just stop"
        @echo "  log -- tmux change to log dir -- just log xinshou" 
        @echo "  tailf -- tail log -- just tailf xinshou filename [key1] [key2]"
        @echo "  diff -- diff two file -- just diff file1 file2"
        @echo "  dump -- print the traceback" >/dev/null
        @echo "  clear -- rm all log and run clear command" >/dev/null
        @echo 

