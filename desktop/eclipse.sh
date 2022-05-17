#!/bin/bash

BASE="/home/metastable/workspaces"

PLATFORM=$1
PERSPECTIVE=$2

ECLIPSE_HOME="/home/metastable/opt/eclipse"
ECLIPSE="current/eclipse"

ADD_PATH="/home/metastable/bin"
ECLIPSE_OPTS="-vmargs -Djava.library.path=/usr/lib/jvm/jdk-8-oracle/lib/amd64"

DATA="$BASE/$PERSPECTIVE"

if [ "$PLATFORM" = "spring" ]
then
	ECLIPSE_HOME="/home/metastable/opt/spring"
	ECLIPSE="current/SpringToolSuite4"
	
	ADD_PATH="/home/metastable/bin"
	ECLIPSE_OPTS="-vmargs -Djava.library.path=/usr/lib/jvm/jdk-8-oracle/lib/amd64"
elif [ "$PLATFORM" = "php" ]
then
	ECLIPSE_HOME="/home/metastable/opt/eclipse"
	ECLIPSE="php-2020-06/eclipse"
	DATA="$BASE/php"
else
	ECLIPSE_HOME="/home/metastable/opt/eclipse"
	ECLIPSE="current_jee/eclipse"
fi

if [ "$PERSPECTIVE" = "digipolis/6.5.0.1" ]
then
	DATA="$BASE/inuits/digipolis/6.5.0.1"
	ADD_PATH="/home/metastable/bin"
	ECLIPSE_OPTS="-vmargs -Djava.library.path=/usr/lib/jvm/java-11-openjdk-amd64"
elif [ "$PERSPECTIVE" = "digipolis/6.6.0" ]
then
	DATA="$BASE/inuits/digipolis/6.6.0"
	ADD_PATH="/home/metastable/bin"
	ECLIPSE_OPTS="-vmargs -Djava.library.path=/usr/lib/jvm/java-11-openjdk-amd64"
elif [ "$PERSPECTIVE" = "digipolis/6.7.0" ]
then
	DATA="$BASE/inuits/digipolis/6.7.0"
	ADD_PATH="/home/metastable/bin"
	ECLIPSE_OPTS="-vmargs -Djava.library.path=/usr/lib/jvm/java-11-openjdk-amd64"
elif [ "$PERSPECTIVE" = "pearlchain" ]
then
	DATA="$BASE/pearlchain/work/workspaces/pearlchainCoffeeRoots"
fi

ECLIPSE="$ECLIPSE_HOME/$ECLIPSE -data $DATA $ECLIPSE_OPTS"
echo "Running $ECLIPSE"

$ECLIPSE
