Name     : apache-spark
Version  : 2.0.0
Release  : 10
URL      : http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0.tgz
Source0  : http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0.tgz
Source1  : spark-script
Patch0   : 0001-Properly-style-for-pom.patch
Patch1   : 0001-Add-leveldb-in-network-shuffle.patch
Patch2   : 0001-Add-javax.ws.rs-in-core-pom.xml.patch
Patch3   : 0001-Add-slf4j-dep-to-flume-sink.patch
Patch4   : 0001-Add-htmlunit-to-core-pom.xml.patch
Patch5   : 0001-Add-avro-to-flume-sink-pom.patch
Patch6   : 0001-Add-flume-to-flume-sink.patch
Patch7   : 0001-Import-GzipHandler-from-jetty-new-version.patch
Summary  : R Frontend for Apache Spark
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause BSD-4-Clause-UC CDDL-1.0 ECL-2.0 HPND MIT PostgreSQL Python-2.0
Requires : apache-spark-bin
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-JavaEWAH
BuildRequires : jdk-RoaringBitmap
BuildRequires : jdk-ST4
BuildRequires : jdk-aether
BuildRequires : jdk-antlr
BuildRequires : jdk-antlr3
BuildRequires : jdk-antlr4
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-log4j-extras
BuildRequires : jdk-apache-parent
BuildRequires : jdk-apache-resource-bundles
BuildRequires : jdk-arpack_combined_all
BuildRequires : jdk-atinject
BuildRequires : jdk-avro
BuildRequires : jdk-bonecp
BuildRequires : jdk-bonecp-parent
BuildRequires : jdk-breeze-macros_2.11
BuildRequires : jdk-breeze_2.11
BuildRequires : jdk-bsh
BuildRequires : jdk-build-helper-maven-plugin
BuildRequires : jdk-calcite
BuildRequires : jdk-cdi-api
BuildRequires : jdk-cglib
BuildRequires : jdk-checkstyle
BuildRequires : jdk-chill-java
BuildRequires : jdk-chill_2.11
BuildRequires : jdk-classutil_2.11
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-configuration
BuildRequires : jdk-commons-dbcp
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-exec
BuildRequires : jdk-commons-httpclient
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-math
BuildRequires : jdk-commons-math3
BuildRequires : jdk-commons-net
BuildRequires : jdk-commons-parent
BuildRequires : jdk-commons-pool
BuildRequires : jdk-commons-validator
BuildRequires : jdk-compiler-interface
BuildRequires : jdk-compress-lzf
BuildRequires : jdk-cssparser
BuildRequires : jdk-curator
BuildRequires : jdk-datanucleus-api-jdo
BuildRequires : jdk-datanucleus-core
BuildRequires : jdk-datanucleus-rdbms
BuildRequires : jdk-derby
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-integration-tools
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-eclipse-jetty-parent
BuildRequires : jdk-enforcer
BuildRequires : jdk-fasterxml-oss-parent
BuildRequires : jdk-file-management
BuildRequires : jdk-flume-ng
BuildRequires : jdk-flume-parent
BuildRequires : jdk-glassfish-servlet-api
BuildRequires : jdk-google
BuildRequires : jdk-grizzled-scala_2.11
BuildRequires : jdk-grizzled-slf4j_2.11
BuildRequires : jdk-gson
BuildRequires : jdk-guava
BuildRequires : jdk-guava14
BuildRequires : jdk-guice
BuildRequires : jdk-h2
BuildRequires : jdk-hadoop-jars
BuildRequires : jdk-hamcrest
BuildRequires : jdk-hawtjni-project
BuildRequires : jdk-hive
BuildRequires : jdk-htmlunit
BuildRequires : jdk-htmlunit-core-js
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-incremental-compiler
BuildRequires : jdk-ivy
BuildRequires : jdk-jackson-annotations
BuildRequires : jdk-jackson-core
BuildRequires : jdk-jackson-core-asl
BuildRequires : jdk-jackson-databind
BuildRequires : jdk-jackson-mapper-asl
BuildRequires : jdk-jackson-module-paranamer
BuildRequires : jdk-jackson-module-scala
BuildRequires : jdk-jackson-parent
BuildRequires : jdk-jakarta-oro
BuildRequires : jdk-janino
BuildRequires : jdk-jansi
BuildRequires : jdk-jansi-native
BuildRequires : jdk-javassist
BuildRequires : jdk-javax.ws.rs-api
BuildRequires : jdk-javolution
BuildRequires : jdk-jdependency
BuildRequires : jdk-jdo-api
BuildRequires : jdk-jdom
BuildRequires : jdk-jersey-common
BuildRequires : jdk-jersey-containers
BuildRequires : jdk-jersey-core
BuildRequires : jdk-jersey-project
BuildRequires : jdk-jets3t
BuildRequires : jdk-jetty
BuildRequires : jdk-jline
BuildRequires : jdk-jna
BuildRequires : jdk-joda-time
BuildRequires : jdk-jodd
BuildRequires : jdk-jopt-simple
BuildRequires : jdk-jpmml-model
BuildRequires : jdk-json
BuildRequires : jdk-json4s-ast_2.11
BuildRequires : jdk-json4s-core_2.11
BuildRequires : jdk-json4s-jackson_2.11
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-jta
BuildRequires : jdk-jtransforms
BuildRequires : jdk-junit-interface
BuildRequires : jdk-junit-interface
BuildRequires : jdk-junit4
BuildRequires : jdk-jvnet-parent
BuildRequires : jdk-kafka-clients
BuildRequires : jdk-kafka-clients8
BuildRequires : jdk-kafka_2.11
BuildRequires : jdk-kafka_2.118
BuildRequires : jdk-kryo
BuildRequires : jdk-leveldb
BuildRequires : jdk-leveldbjni
BuildRequires : jdk-libfb303
BuildRequires : jdk-libthrift
BuildRequires : jdk-log4j
BuildRequires : jdk-log4j1.2
BuildRequires : jdk-lz4
BuildRequires : jdk-maven-antrun-plugin
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-artifact-resolver
BuildRequires : jdk-maven-assembly-plugin
BuildRequires : jdk-maven-checkstyle-plugin
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-analyzer
BuildRequires : jdk-maven-dependency-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-parent
BuildRequires : jdk-maven-plugin-testing
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-remote-resources-plugin
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-exec
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shade-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-io
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-maven-site-plugin
BuildRequires : jdk-maven-source-plugin
BuildRequires : jdk-mesos
BuildRequires : jdk-metrics
BuildRequires : jdk-minlog
BuildRequires : jdk-mockito
BuildRequires : jdk-mortbay-jetty
BuildRequires : jdk-mysql-connector-java
BuildRequires : jdk-nekohtml
BuildRequires : jdk-netlib-core
BuildRequires : jdk-netty
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-objenesis
BuildRequires : jdk-opencsv
BuildRequires : jdk-paranamer
BuildRequires : jdk-parboiled
BuildRequires : jdk-parquet
BuildRequires : jdk-parquet-format
BuildRequires : jdk-parquet-twitter
BuildRequires : jdk-pegdown
BuildRequires : jdk-pgjdbc
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-resources
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-pmml-model
BuildRequires : jdk-postgresql
BuildRequires : jdk-protobuf-java
BuildRequires : jdk-py4j
BuildRequires : jdk-pyrolite
BuildRequires : jdk-sac
BuildRequires : jdk-sbt-test-interface
BuildRequires : jdk-scala-async_2.11
BuildRequires : jdk-scala-compiler
BuildRequires : jdk-scala-library
BuildRequires : jdk-scala-library2.10
BuildRequires : jdk-scala-maven-plugin
BuildRequires : jdk-scala-parser-combinators_2.11
BuildRequires : jdk-scala-reflect
BuildRequires : jdk-scala-xml_2.11
BuildRequires : jdk-scalacheck_2.11
BuildRequires : jdk-scalap
BuildRequires : jdk-scalariform
BuildRequires : jdk-scalastyle-maven-plugin
BuildRequires : jdk-scalastyle_2.11
BuildRequires : jdk-scalatest-maven-plugin
BuildRequires : jdk-scalatest_2.11
BuildRequires : jdk-scopt_2.11
BuildRequires : jdk-selenium
BuildRequires : jdk-sisu
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy
BuildRequires : jdk-snappy-java
BuildRequires : jdk-sonatype-oss-parent
BuildRequires : jdk-spark-unused
BuildRequires : jdk-spire-macros_2.11
BuildRequires : jdk-spire_2.11
BuildRequires : jdk-stax-api
BuildRequires : jdk-stream
BuildRequires : jdk-surefire
BuildRequires : jdk-treelayout
BuildRequires : jdk-typesafe-config
BuildRequires : jdk-typesafe-sbt-interface
BuildRequires : jdk-univocity-parsers
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-webbit
BuildRequires : jdk-xalan-j2
BuildRequires : jdk-xbean
BuildRequires : jdk-xbean-asm5-shaded
BuildRequires : jdk-xerces-j2
BuildRequires : jdk-xml-apis
BuildRequires : jdk-xmlenc
BuildRequires : jdk-xmlunit
BuildRequires : jdk-xz
BuildRequires : jdk-yammer-metrics
BuildRequires : jdk-zinc
BuildRequires : jdk-zkclient
BuildRequires : jdk-zookeeper
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
This is an assembly module for Spark project.
It creates a single tar.gz file that includes all needed dependency of the project
except for org.apache.hadoop.* jars that are supposed to be available from the
deployed Hadoop cluster.

%package bin
Summary: bin components for the apache-spark package.
Group: Binaries

%description bin
bin components for the apache-spark package.

%prep
%setup -q -n spark-2.0.0
%patch0 -p1 
%patch1 -p1 
%patch2 -p1 
%patch3 -p1 
%patch4 -p1 
%patch5 -p1 
%patch6 -p1 
%patch7 -p1 

%build
# Specify to Xmvn where the jars should be installed.
python3 /usr/share/java-utils/mvn_file.py ":{*}:jar:" spark/@1 /usr/share/apache-spark/jars/@1
python3 /usr/share/java-utils/mvn_build.py -X -- -Dmaven.test.failure.ignore=true

%install
xmvn-install  -R .xmvn-reactor -n apache-spark -d %{buildroot}

# Remove unnecesary cmd
find bin/ -iname *.cmd -delete

# Copy directories
cp -R R/ bin/ conf/ data/ licenses/ python/ sbin/ yarn/ %{buildroot}/usr/share/apache-spark 
rm assembly/target/scala-2.11/jars/spark-*
cp assembly/target/scala-2.11/jars/* %{buildroot}/usr/share/apache-spark/jars
mkdir -p %{buildroot}/usr/share/apache-spark/examples/
mv examples/target/scala-2.11/jars %{buildroot}/usr/share/apache-spark/examples/
mv examples/src %{buildroot}/usr/share/apache-spark/examples/

# Add helper scripts
mkdir -p %{buildroot}/usr/bin
for cmd in beeline pyspark spark-class spark-shell spark-sql spark-submit sparkR
do 
    sed s/@@CMD@@/$cmd/ %{SOURCE1} >%{buildroot}/usr/bin/$cmd
    chmod +x %{buildroot}/usr/bin/$cmd
done

echo "Spark 2.0.0" > %{buildroot}/usr/share/apache-spark/RELEASE

%files bin
%defattr(-,root,root,-)
/usr/bin/beeline
/usr/bin/pyspark
/usr/bin/spark-class
/usr/bin/spark-shell
/usr/bin/spark-sql
/usr/bin/spark-submit
/usr/bin/sparkR
/usr/share/apache-spark/bin/beeline
/usr/share/apache-spark/bin/load-spark-env.sh
/usr/share/apache-spark/bin/pyspark
/usr/share/apache-spark/bin/run-example
/usr/share/apache-spark/bin/spark-class
/usr/share/apache-spark/bin/spark-shell
/usr/share/apache-spark/bin/spark-sql
/usr/share/apache-spark/bin/spark-submit
/usr/share/apache-spark/bin/sparkR

%files
%defattr(-,root,root,-)
%exclude /usr/share/apache-spark/R/.gitignore
/usr/share/apache-spark/RELEASE
/usr/share/apache-spark/R/DOCUMENTATION.md
/usr/share/apache-spark/R/README.md
/usr/share/apache-spark/R/WINDOWS.md
/usr/share/apache-spark/R/check-cran.sh
/usr/share/apache-spark/R/create-docs.sh
/usr/share/apache-spark/R/install-dev.bat
/usr/share/apache-spark/R/install-dev.sh
/usr/share/apache-spark/R/log4j.properties
/usr/share/apache-spark/R/pkg/.Rbuildignore
/usr/share/apache-spark/R/pkg/.lintr
/usr/share/apache-spark/R/pkg/DESCRIPTION
/usr/share/apache-spark/R/pkg/NAMESPACE
/usr/share/apache-spark/R/pkg/R/DataFrame.R
/usr/share/apache-spark/R/pkg/R/RDD.R
/usr/share/apache-spark/R/pkg/R/SQLContext.R
/usr/share/apache-spark/R/pkg/R/WindowSpec.R
/usr/share/apache-spark/R/pkg/R/backend.R
/usr/share/apache-spark/R/pkg/R/broadcast.R
/usr/share/apache-spark/R/pkg/R/client.R
/usr/share/apache-spark/R/pkg/R/column.R
/usr/share/apache-spark/R/pkg/R/context.R
/usr/share/apache-spark/R/pkg/R/deserialize.R
/usr/share/apache-spark/R/pkg/R/functions.R
/usr/share/apache-spark/R/pkg/R/generics.R
/usr/share/apache-spark/R/pkg/R/group.R
/usr/share/apache-spark/R/pkg/R/jobj.R
/usr/share/apache-spark/R/pkg/R/mllib.R
/usr/share/apache-spark/R/pkg/R/pairRDD.R
/usr/share/apache-spark/R/pkg/R/schema.R
/usr/share/apache-spark/R/pkg/R/serialize.R
/usr/share/apache-spark/R/pkg/R/sparkR.R
/usr/share/apache-spark/R/pkg/R/stats.R
/usr/share/apache-spark/R/pkg/R/types.R
/usr/share/apache-spark/R/pkg/R/utils.R
/usr/share/apache-spark/R/pkg/R/window.R
/usr/share/apache-spark/R/pkg/inst/profile/general.R
/usr/share/apache-spark/R/pkg/inst/profile/shell.R
/usr/share/apache-spark/R/pkg/inst/test_support/sparktestjar_2.10-1.0.jar
/usr/share/apache-spark/R/pkg/inst/tests/testthat/jarTest.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/packageInAJarTest.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_Serde.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_Windows.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_binaryFile.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_binary_function.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_broadcast.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_client.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_context.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_includeJAR.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_includePackage.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_mllib.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_parallelize_collect.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_rdd.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_shuffle.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_sparkSQL.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_take.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_textFile.R
/usr/share/apache-spark/R/pkg/inst/tests/testthat/test_utils.R
/usr/share/apache-spark/R/pkg/inst/worker/daemon.R
/usr/share/apache-spark/R/pkg/inst/worker/worker.R
/usr/share/apache-spark/R/pkg/src-native/Makefile
/usr/share/apache-spark/R/pkg/src-native/Makefile.win
/usr/share/apache-spark/R/pkg/src-native/string_hash_code.c
/usr/share/apache-spark/R/pkg/tests/run-all.R
/usr/share/apache-spark/R/run-tests.sh
/usr/share/apache-spark/conf/docker.properties.template
/usr/share/apache-spark/conf/fairscheduler.xml.template
/usr/share/apache-spark/conf/log4j.properties.template
/usr/share/apache-spark/conf/metrics.properties.template
/usr/share/apache-spark/conf/slaves.template
/usr/share/apache-spark/conf/spark-defaults.conf.template
/usr/share/apache-spark/conf/spark-env.sh.template
/usr/share/apache-spark/data/graphx/followers.txt
/usr/share/apache-spark/data/graphx/users.txt
/usr/share/apache-spark/data/mllib/als/sample_movielens_ratings.txt
/usr/share/apache-spark/data/mllib/als/test.data
/usr/share/apache-spark/data/mllib/gmm_data.txt
/usr/share/apache-spark/data/mllib/kmeans_data.txt
/usr/share/apache-spark/data/mllib/lr-data/random.data
/usr/share/apache-spark/data/mllib/lr_data.txt
/usr/share/apache-spark/data/mllib/pagerank_data.txt
/usr/share/apache-spark/data/mllib/pic_data.txt
/usr/share/apache-spark/data/mllib/ridge-data/lpsa.data
/usr/share/apache-spark/data/mllib/sample_binary_classification_data.txt
/usr/share/apache-spark/data/mllib/sample_fpgrowth.txt
/usr/share/apache-spark/data/mllib/sample_isotonic_regression_libsvm_data.txt
/usr/share/apache-spark/data/mllib/sample_kmeans_data.txt
/usr/share/apache-spark/data/mllib/sample_lda_data.txt
/usr/share/apache-spark/data/mllib/sample_lda_libsvm_data.txt
/usr/share/apache-spark/data/mllib/sample_libsvm_data.txt
/usr/share/apache-spark/data/mllib/sample_linear_regression_data.txt
/usr/share/apache-spark/data/mllib/sample_movielens_data.txt
/usr/share/apache-spark/data/mllib/sample_multiclass_classification_data.txt
/usr/share/apache-spark/data/mllib/sample_svm_data.txt
/usr/share/apache-spark/data/mllib/sample_tree_data.csv
/usr/share/apache-spark/data/mllib/streaming_kmeans_data_test.txt
/usr/share/apache-spark/data/streaming/AFINN-111.txt
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/JavaHdfsLR.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/JavaLogQuery.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/JavaPageRank.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/JavaSparkPi.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/JavaStatusTrackerDemo.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/JavaTC.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/JavaWordCount.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaAFTSurvivalRegressionExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaALSExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaBinarizerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaBisectingKMeansExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaBucketizerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaChiSqSelectorExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaCountVectorizerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaDCTExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaDecisionTreeClassificationExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaDecisionTreeRegressionExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaDocument.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaElementwiseProductExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaEstimatorTransformerParamExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaGaussianMixtureExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaGeneralizedLinearRegressionExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaGradientBoostedTreeClassifierExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaGradientBoostedTreeRegressorExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaIndexToStringExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaIsotonicRegressionExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaKMeansExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaLDAExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaLabeledDocument.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaLinearRegressionWithElasticNetExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaLogisticRegressionSummaryExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaLogisticRegressionWithElasticNetExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaMaxAbsScalerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaMinMaxScalerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaModelSelectionViaCrossValidationExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaModelSelectionViaTrainValidationSplitExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaMultilayerPerceptronClassifierExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaNGramExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaNaiveBayesExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaNormalizerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaOneHotEncoderExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaOneVsRestExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaPCAExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaPipelineExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaPolynomialExpansionExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaQuantileDiscretizerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaRFormulaExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaRandomForestClassifierExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaRandomForestRegressorExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaSQLTransformerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaSimpleParamsExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaSimpleTextClassificationPipeline.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaStandardScalerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaStopWordsRemoverExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaStringIndexerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaTfIdfExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaTokenizerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaVectorAssemblerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaVectorIndexerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaVectorSlicerExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/ml/JavaWord2VecExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaALS.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaAssociationRulesExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaBinaryClassificationMetricsExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaBisectingKMeansExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaChiSqSelectorExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaCorrelationsExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaDecisionTreeClassificationExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaDecisionTreeRegressionExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaElementwiseProductExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaGaussianMixtureExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaGradientBoostingClassificationExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaGradientBoostingRegressionExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaHypothesisTestingExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaHypothesisTestingKolmogorovSmirnovTestExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaIsotonicRegressionExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaKMeansExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaKernelDensityEstimationExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaLBFGSExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaLatentDirichletAllocationExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaLinearRegressionWithSGDExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaLogisticRegressionWithLBFGSExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaMultiLabelClassificationMetricsExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaMulticlassClassificationMetricsExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaNaiveBayesExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaPCAExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaPowerIterationClusteringExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaPrefixSpanExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaRandomForestClassificationExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaRandomForestRegressionExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaRankingMetricsExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaRecommendationExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaRegressionMetricsExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaSVDExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaSVMWithSGDExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaSimpleFPGrowth.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaStratifiedSamplingExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaStreamingTestExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/mllib/JavaSummaryStatisticsExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/sql/JavaSQLDataSourceExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/sql/JavaSparkSQLExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/sql/hive/JavaSparkHiveExample.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/sql/streaming/JavaStructuredNetworkWordCount.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/sql/streaming/JavaStructuredNetworkWordCountWindowed.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/streaming/JavaCustomReceiver.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/streaming/JavaDirectKafkaWordCount.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/streaming/JavaFlumeEventCount.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/streaming/JavaKafkaWordCount.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/streaming/JavaNetworkWordCount.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/streaming/JavaQueueStream.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/streaming/JavaRecord.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/streaming/JavaRecoverableNetworkWordCount.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/streaming/JavaSqlNetworkWordCount.java
/usr/share/apache-spark/examples/src/main/java/org/apache/spark/examples/streaming/JavaStatefulNetworkWordCount.java
/usr/share/apache-spark/examples/src/main/python/als.py
/usr/share/apache-spark/examples/src/main/python/als.pyc
/usr/share/apache-spark/examples/src/main/python/als.pyo
/usr/share/apache-spark/examples/src/main/python/avro_inputformat.py
/usr/share/apache-spark/examples/src/main/python/avro_inputformat.pyc
/usr/share/apache-spark/examples/src/main/python/avro_inputformat.pyo
/usr/share/apache-spark/examples/src/main/python/kmeans.py
/usr/share/apache-spark/examples/src/main/python/kmeans.pyc
/usr/share/apache-spark/examples/src/main/python/kmeans.pyo
/usr/share/apache-spark/examples/src/main/python/logistic_regression.py
/usr/share/apache-spark/examples/src/main/python/logistic_regression.pyc
/usr/share/apache-spark/examples/src/main/python/logistic_regression.pyo
/usr/share/apache-spark/examples/src/main/python/ml/aft_survival_regression.py
/usr/share/apache-spark/examples/src/main/python/ml/aft_survival_regression.pyc
/usr/share/apache-spark/examples/src/main/python/ml/aft_survival_regression.pyo
/usr/share/apache-spark/examples/src/main/python/ml/als_example.py
/usr/share/apache-spark/examples/src/main/python/ml/als_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/als_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/binarizer_example.py
/usr/share/apache-spark/examples/src/main/python/ml/binarizer_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/binarizer_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/bisecting_k_means_example.py
/usr/share/apache-spark/examples/src/main/python/ml/bisecting_k_means_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/bisecting_k_means_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/bucketizer_example.py
/usr/share/apache-spark/examples/src/main/python/ml/bucketizer_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/bucketizer_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/chisq_selector_example.py
/usr/share/apache-spark/examples/src/main/python/ml/chisq_selector_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/chisq_selector_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/count_vectorizer_example.py
/usr/share/apache-spark/examples/src/main/python/ml/count_vectorizer_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/count_vectorizer_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/cross_validator.py
/usr/share/apache-spark/examples/src/main/python/ml/cross_validator.pyc
/usr/share/apache-spark/examples/src/main/python/ml/cross_validator.pyo
/usr/share/apache-spark/examples/src/main/python/ml/dataframe_example.py
/usr/share/apache-spark/examples/src/main/python/ml/dataframe_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/dataframe_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/dct_example.py
/usr/share/apache-spark/examples/src/main/python/ml/dct_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/dct_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/decision_tree_classification_example.py
/usr/share/apache-spark/examples/src/main/python/ml/decision_tree_classification_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/decision_tree_classification_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/decision_tree_regression_example.py
/usr/share/apache-spark/examples/src/main/python/ml/decision_tree_regression_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/decision_tree_regression_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/elementwise_product_example.py
/usr/share/apache-spark/examples/src/main/python/ml/elementwise_product_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/elementwise_product_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/estimator_transformer_param_example.py
/usr/share/apache-spark/examples/src/main/python/ml/estimator_transformer_param_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/estimator_transformer_param_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/gaussian_mixture_example.py
/usr/share/apache-spark/examples/src/main/python/ml/gaussian_mixture_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/gaussian_mixture_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/generalized_linear_regression_example.py
/usr/share/apache-spark/examples/src/main/python/ml/generalized_linear_regression_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/generalized_linear_regression_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/gradient_boosted_tree_classifier_example.py
/usr/share/apache-spark/examples/src/main/python/ml/gradient_boosted_tree_classifier_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/gradient_boosted_tree_classifier_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/gradient_boosted_tree_regressor_example.py
/usr/share/apache-spark/examples/src/main/python/ml/gradient_boosted_tree_regressor_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/gradient_boosted_tree_regressor_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/index_to_string_example.py
/usr/share/apache-spark/examples/src/main/python/ml/index_to_string_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/index_to_string_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/isotonic_regression_example.py
/usr/share/apache-spark/examples/src/main/python/ml/isotonic_regression_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/isotonic_regression_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/kmeans_example.py
/usr/share/apache-spark/examples/src/main/python/ml/kmeans_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/kmeans_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/lda_example.py
/usr/share/apache-spark/examples/src/main/python/ml/lda_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/lda_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/linear_regression_with_elastic_net.py
/usr/share/apache-spark/examples/src/main/python/ml/linear_regression_with_elastic_net.pyc
/usr/share/apache-spark/examples/src/main/python/ml/linear_regression_with_elastic_net.pyo
/usr/share/apache-spark/examples/src/main/python/ml/logistic_regression_with_elastic_net.py
/usr/share/apache-spark/examples/src/main/python/ml/logistic_regression_with_elastic_net.pyc
/usr/share/apache-spark/examples/src/main/python/ml/logistic_regression_with_elastic_net.pyo
/usr/share/apache-spark/examples/src/main/python/ml/max_abs_scaler_example.py
/usr/share/apache-spark/examples/src/main/python/ml/max_abs_scaler_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/max_abs_scaler_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/min_max_scaler_example.py
/usr/share/apache-spark/examples/src/main/python/ml/min_max_scaler_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/min_max_scaler_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/multilayer_perceptron_classification.py
/usr/share/apache-spark/examples/src/main/python/ml/multilayer_perceptron_classification.pyc
/usr/share/apache-spark/examples/src/main/python/ml/multilayer_perceptron_classification.pyo
/usr/share/apache-spark/examples/src/main/python/ml/n_gram_example.py
/usr/share/apache-spark/examples/src/main/python/ml/n_gram_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/n_gram_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/naive_bayes_example.py
/usr/share/apache-spark/examples/src/main/python/ml/naive_bayes_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/naive_bayes_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/normalizer_example.py
/usr/share/apache-spark/examples/src/main/python/ml/normalizer_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/normalizer_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/one_vs_rest_example.py
/usr/share/apache-spark/examples/src/main/python/ml/one_vs_rest_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/one_vs_rest_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/onehot_encoder_example.py
/usr/share/apache-spark/examples/src/main/python/ml/onehot_encoder_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/onehot_encoder_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/pca_example.py
/usr/share/apache-spark/examples/src/main/python/ml/pca_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/pca_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/pipeline_example.py
/usr/share/apache-spark/examples/src/main/python/ml/pipeline_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/pipeline_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/polynomial_expansion_example.py
/usr/share/apache-spark/examples/src/main/python/ml/polynomial_expansion_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/polynomial_expansion_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/quantile_discretizer_example.py
/usr/share/apache-spark/examples/src/main/python/ml/quantile_discretizer_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/quantile_discretizer_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/random_forest_classifier_example.py
/usr/share/apache-spark/examples/src/main/python/ml/random_forest_classifier_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/random_forest_classifier_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/random_forest_regressor_example.py
/usr/share/apache-spark/examples/src/main/python/ml/random_forest_regressor_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/random_forest_regressor_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/rformula_example.py
/usr/share/apache-spark/examples/src/main/python/ml/rformula_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/rformula_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/simple_params_example.py
/usr/share/apache-spark/examples/src/main/python/ml/simple_params_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/simple_params_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/simple_text_classification_pipeline.py
/usr/share/apache-spark/examples/src/main/python/ml/simple_text_classification_pipeline.pyc
/usr/share/apache-spark/examples/src/main/python/ml/simple_text_classification_pipeline.pyo
/usr/share/apache-spark/examples/src/main/python/ml/sql_transformer.py
/usr/share/apache-spark/examples/src/main/python/ml/sql_transformer.pyc
/usr/share/apache-spark/examples/src/main/python/ml/sql_transformer.pyo
/usr/share/apache-spark/examples/src/main/python/ml/standard_scaler_example.py
/usr/share/apache-spark/examples/src/main/python/ml/standard_scaler_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/standard_scaler_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/stopwords_remover_example.py
/usr/share/apache-spark/examples/src/main/python/ml/stopwords_remover_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/stopwords_remover_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/string_indexer_example.py
/usr/share/apache-spark/examples/src/main/python/ml/string_indexer_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/string_indexer_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/tf_idf_example.py
/usr/share/apache-spark/examples/src/main/python/ml/tf_idf_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/tf_idf_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/tokenizer_example.py
/usr/share/apache-spark/examples/src/main/python/ml/tokenizer_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/tokenizer_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/train_validation_split.py
/usr/share/apache-spark/examples/src/main/python/ml/train_validation_split.pyc
/usr/share/apache-spark/examples/src/main/python/ml/train_validation_split.pyo
/usr/share/apache-spark/examples/src/main/python/ml/vector_assembler_example.py
/usr/share/apache-spark/examples/src/main/python/ml/vector_assembler_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/vector_assembler_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/vector_indexer_example.py
/usr/share/apache-spark/examples/src/main/python/ml/vector_indexer_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/vector_indexer_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/vector_slicer_example.py
/usr/share/apache-spark/examples/src/main/python/ml/vector_slicer_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/vector_slicer_example.pyo
/usr/share/apache-spark/examples/src/main/python/ml/word2vec_example.py
/usr/share/apache-spark/examples/src/main/python/ml/word2vec_example.pyc
/usr/share/apache-spark/examples/src/main/python/ml/word2vec_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/binary_classification_metrics_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/binary_classification_metrics_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/binary_classification_metrics_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/bisecting_k_means_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/bisecting_k_means_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/bisecting_k_means_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/correlations.py
/usr/share/apache-spark/examples/src/main/python/mllib/correlations.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/correlations.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/correlations_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/correlations_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/correlations_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/decision_tree_classification_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/decision_tree_classification_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/decision_tree_classification_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/decision_tree_regression_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/decision_tree_regression_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/decision_tree_regression_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/elementwise_product_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/elementwise_product_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/elementwise_product_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/fpgrowth_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/fpgrowth_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/fpgrowth_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/gaussian_mixture_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/gaussian_mixture_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/gaussian_mixture_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/gaussian_mixture_model.py
/usr/share/apache-spark/examples/src/main/python/mllib/gaussian_mixture_model.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/gaussian_mixture_model.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/gradient_boosting_classification_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/gradient_boosting_classification_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/gradient_boosting_classification_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/gradient_boosting_regression_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/gradient_boosting_regression_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/gradient_boosting_regression_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/hypothesis_testing_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/hypothesis_testing_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/hypothesis_testing_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/hypothesis_testing_kolmogorov_smirnov_test_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/hypothesis_testing_kolmogorov_smirnov_test_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/hypothesis_testing_kolmogorov_smirnov_test_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/isotonic_regression_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/isotonic_regression_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/isotonic_regression_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/k_means_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/k_means_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/k_means_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/kernel_density_estimation_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/kernel_density_estimation_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/kernel_density_estimation_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/kmeans.py
/usr/share/apache-spark/examples/src/main/python/mllib/kmeans.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/kmeans.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/latent_dirichlet_allocation_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/latent_dirichlet_allocation_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/latent_dirichlet_allocation_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/linear_regression_with_sgd_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/linear_regression_with_sgd_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/linear_regression_with_sgd_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/logistic_regression.py
/usr/share/apache-spark/examples/src/main/python/mllib/logistic_regression.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/logistic_regression.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/logistic_regression_with_lbfgs_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/logistic_regression_with_lbfgs_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/logistic_regression_with_lbfgs_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/multi_class_metrics_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/multi_class_metrics_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/multi_class_metrics_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/multi_label_metrics_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/multi_label_metrics_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/multi_label_metrics_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/naive_bayes_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/naive_bayes_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/naive_bayes_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/normalizer_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/normalizer_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/normalizer_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/power_iteration_clustering_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/power_iteration_clustering_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/power_iteration_clustering_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/random_forest_classification_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/random_forest_classification_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/random_forest_classification_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/random_forest_regression_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/random_forest_regression_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/random_forest_regression_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/random_rdd_generation.py
/usr/share/apache-spark/examples/src/main/python/mllib/random_rdd_generation.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/random_rdd_generation.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/ranking_metrics_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/ranking_metrics_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/ranking_metrics_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/recommendation_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/recommendation_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/recommendation_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/regression_metrics_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/regression_metrics_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/regression_metrics_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/sampled_rdds.py
/usr/share/apache-spark/examples/src/main/python/mllib/sampled_rdds.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/sampled_rdds.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/standard_scaler_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/standard_scaler_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/standard_scaler_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/stratified_sampling_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/stratified_sampling_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/stratified_sampling_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/streaming_k_means_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/streaming_k_means_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/streaming_k_means_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/streaming_linear_regression_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/streaming_linear_regression_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/streaming_linear_regression_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/summary_statistics_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/summary_statistics_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/summary_statistics_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/svm_with_sgd_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/svm_with_sgd_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/svm_with_sgd_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/tf_idf_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/tf_idf_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/tf_idf_example.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/word2vec.py
/usr/share/apache-spark/examples/src/main/python/mllib/word2vec.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/word2vec.pyo
/usr/share/apache-spark/examples/src/main/python/mllib/word2vec_example.py
/usr/share/apache-spark/examples/src/main/python/mllib/word2vec_example.pyc
/usr/share/apache-spark/examples/src/main/python/mllib/word2vec_example.pyo
/usr/share/apache-spark/examples/src/main/python/pagerank.py
/usr/share/apache-spark/examples/src/main/python/pagerank.pyc
/usr/share/apache-spark/examples/src/main/python/pagerank.pyo
/usr/share/apache-spark/examples/src/main/python/parquet_inputformat.py
/usr/share/apache-spark/examples/src/main/python/parquet_inputformat.pyc
/usr/share/apache-spark/examples/src/main/python/parquet_inputformat.pyo
/usr/share/apache-spark/examples/src/main/python/pi.py
/usr/share/apache-spark/examples/src/main/python/pi.pyc
/usr/share/apache-spark/examples/src/main/python/pi.pyo
/usr/share/apache-spark/examples/src/main/python/sort.py
/usr/share/apache-spark/examples/src/main/python/sort.pyc
/usr/share/apache-spark/examples/src/main/python/sort.pyo
/usr/share/apache-spark/examples/src/main/python/sql.py
/usr/share/apache-spark/examples/src/main/python/sql.pyc
/usr/share/apache-spark/examples/src/main/python/sql.pyo
/usr/share/apache-spark/examples/src/main/python/sql/streaming/structured_network_wordcount.py
/usr/share/apache-spark/examples/src/main/python/sql/streaming/structured_network_wordcount.pyc
/usr/share/apache-spark/examples/src/main/python/sql/streaming/structured_network_wordcount.pyo
/usr/share/apache-spark/examples/src/main/python/sql/streaming/structured_network_wordcount_windowed.py
/usr/share/apache-spark/examples/src/main/python/sql/streaming/structured_network_wordcount_windowed.pyc
/usr/share/apache-spark/examples/src/main/python/sql/streaming/structured_network_wordcount_windowed.pyo
/usr/share/apache-spark/examples/src/main/python/status_api_demo.py
/usr/share/apache-spark/examples/src/main/python/status_api_demo.pyc
/usr/share/apache-spark/examples/src/main/python/status_api_demo.pyo
/usr/share/apache-spark/examples/src/main/python/streaming/direct_kafka_wordcount.py
/usr/share/apache-spark/examples/src/main/python/streaming/direct_kafka_wordcount.pyc
/usr/share/apache-spark/examples/src/main/python/streaming/direct_kafka_wordcount.pyo
/usr/share/apache-spark/examples/src/main/python/streaming/flume_wordcount.py
/usr/share/apache-spark/examples/src/main/python/streaming/flume_wordcount.pyc
/usr/share/apache-spark/examples/src/main/python/streaming/flume_wordcount.pyo
/usr/share/apache-spark/examples/src/main/python/streaming/hdfs_wordcount.py
/usr/share/apache-spark/examples/src/main/python/streaming/hdfs_wordcount.pyc
/usr/share/apache-spark/examples/src/main/python/streaming/hdfs_wordcount.pyo
/usr/share/apache-spark/examples/src/main/python/streaming/kafka_wordcount.py
/usr/share/apache-spark/examples/src/main/python/streaming/kafka_wordcount.pyc
/usr/share/apache-spark/examples/src/main/python/streaming/kafka_wordcount.pyo
/usr/share/apache-spark/examples/src/main/python/streaming/network_wordcount.py
/usr/share/apache-spark/examples/src/main/python/streaming/network_wordcount.pyc
/usr/share/apache-spark/examples/src/main/python/streaming/network_wordcount.pyo
/usr/share/apache-spark/examples/src/main/python/streaming/network_wordjoinsentiments.py
/usr/share/apache-spark/examples/src/main/python/streaming/network_wordjoinsentiments.pyc
/usr/share/apache-spark/examples/src/main/python/streaming/network_wordjoinsentiments.pyo
/usr/share/apache-spark/examples/src/main/python/streaming/queue_stream.py
/usr/share/apache-spark/examples/src/main/python/streaming/queue_stream.pyc
/usr/share/apache-spark/examples/src/main/python/streaming/queue_stream.pyo
/usr/share/apache-spark/examples/src/main/python/streaming/recoverable_network_wordcount.py
/usr/share/apache-spark/examples/src/main/python/streaming/recoverable_network_wordcount.pyc
/usr/share/apache-spark/examples/src/main/python/streaming/recoverable_network_wordcount.pyo
/usr/share/apache-spark/examples/src/main/python/streaming/sql_network_wordcount.py
/usr/share/apache-spark/examples/src/main/python/streaming/sql_network_wordcount.pyc
/usr/share/apache-spark/examples/src/main/python/streaming/sql_network_wordcount.pyo
/usr/share/apache-spark/examples/src/main/python/streaming/stateful_network_wordcount.py
/usr/share/apache-spark/examples/src/main/python/streaming/stateful_network_wordcount.pyc
/usr/share/apache-spark/examples/src/main/python/streaming/stateful_network_wordcount.pyo
/usr/share/apache-spark/examples/src/main/python/transitive_closure.py
/usr/share/apache-spark/examples/src/main/python/transitive_closure.pyc
/usr/share/apache-spark/examples/src/main/python/transitive_closure.pyo
/usr/share/apache-spark/examples/src/main/python/wordcount.py
/usr/share/apache-spark/examples/src/main/python/wordcount.pyc
/usr/share/apache-spark/examples/src/main/python/wordcount.pyo
/usr/share/apache-spark/examples/src/main/r/RSparkSQLExample.R
/usr/share/apache-spark/examples/src/main/r/data-manipulation.R
/usr/share/apache-spark/examples/src/main/r/dataframe.R
/usr/share/apache-spark/examples/src/main/r/ml.R
/usr/share/apache-spark/examples/src/main/resources/full_user.avsc
/usr/share/apache-spark/examples/src/main/resources/kv1.txt
/usr/share/apache-spark/examples/src/main/resources/people.json
/usr/share/apache-spark/examples/src/main/resources/people.txt
/usr/share/apache-spark/examples/src/main/resources/user.avsc
/usr/share/apache-spark/examples/src/main/resources/users.avro
/usr/share/apache-spark/examples/src/main/resources/users.parquet
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/BroadcastTest.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/DFSReadWriteTest.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/DriverSubmissionTest.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ExceptionHandlingTest.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/GroupByTest.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/HdfsTest.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/LocalALS.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/LocalFileLR.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/LocalKMeans.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/LocalLR.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/LocalPi.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/LogQuery.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/MultiBroadcastTest.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/SimpleSkewedGroupByTest.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/SkewedGroupByTest.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/SparkALS.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/SparkHdfsLR.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/SparkKMeans.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/SparkLR.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/SparkPageRank.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/SparkPi.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/SparkTC.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/graphx/AggregateMessagesExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/graphx/Analytics.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/graphx/ComprehensiveExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/graphx/ConnectedComponentsExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/graphx/LiveJournalPageRank.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/graphx/PageRankExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/graphx/SSSPExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/graphx/SynthBenchmark.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/graphx/TriangleCountingExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/AFTSurvivalRegressionExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/ALSExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/BinarizerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/BisectingKMeansExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/BucketizerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/ChiSqSelectorExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/CountVectorizerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/DCTExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/DataFrameExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/DecisionTreeClassificationExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/DecisionTreeExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/DecisionTreeRegressionExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/DeveloperApiExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/ElementwiseProductExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/EstimatorTransformerParamExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/GBTExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/GaussianMixtureExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/GeneralizedLinearRegressionExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/GradientBoostedTreeClassifierExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/GradientBoostedTreeRegressorExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/IndexToStringExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/IsotonicRegressionExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/KMeansExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/LDAExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/LinearRegressionExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/LinearRegressionWithElasticNetExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/LogisticRegressionExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/LogisticRegressionSummaryExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/LogisticRegressionWithElasticNetExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/MaxAbsScalerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/MinMaxScalerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/ModelSelectionViaCrossValidationExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/ModelSelectionViaTrainValidationSplitExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/MultilayerPerceptronClassifierExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/NGramExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/NaiveBayesExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/NormalizerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/OneHotEncoderExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/OneVsRestExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/PCAExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/PipelineExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/PolynomialExpansionExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/QuantileDiscretizerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/RFormulaExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/RandomForestClassifierExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/RandomForestExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/RandomForestRegressorExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/SQLTransformerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/SimpleParamsExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/SimpleTextClassificationPipeline.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/StandardScalerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/StopWordsRemoverExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/StringIndexerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/TfIdfExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/TokenizerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/UnaryTransformerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/VectorAssemblerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/VectorIndexerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/VectorSlicerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/ml/Word2VecExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/AbstractParams.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/AssociationRulesExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/BinaryClassification.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/BinaryClassificationMetricsExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/BisectingKMeansExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/ChiSqSelectorExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/Correlations.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/CorrelationsExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/CosineSimilarity.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/DecisionTreeClassificationExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/DecisionTreeRegressionExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/DecisionTreeRunner.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/DenseGaussianMixture.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/DenseKMeans.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/ElementwiseProductExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/FPGrowthExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/GaussianMixtureExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/GradientBoostedTreesRunner.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/GradientBoostingClassificationExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/GradientBoostingRegressionExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/HypothesisTestingExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/HypothesisTestingKolmogorovSmirnovTestExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/IsotonicRegressionExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/KMeansExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/KernelDensityEstimationExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/LBFGSExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/LDAExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/LatentDirichletAllocationExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/LinearRegression.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/LinearRegressionWithSGDExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/LogisticRegressionWithLBFGSExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/MovieLensALS.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/MultiLabelMetricsExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/MulticlassMetricsExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/MultivariateSummarizer.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/NaiveBayesExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/NormalizerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/PCAExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/PCAOnRowMatrixExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/PCAOnSourceVectorExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/PMMLModelExportExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/PowerIterationClusteringExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/PrefixSpanExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/RandomForestClassificationExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/RandomForestRegressionExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/RandomRDDGeneration.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/RankingMetricsExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/RecommendationExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/RegressionMetricsExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/SVDExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/SVMWithSGDExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/SampledRDDs.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/SimpleFPGrowth.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/SparseNaiveBayes.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/StandardScalerExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/StratifiedSamplingExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/StreamingKMeansExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/StreamingLinearRegression.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/StreamingLinearRegressionExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/StreamingLogisticRegression.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/StreamingTestExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/SummaryStatisticsExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/TFIDFExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/TallSkinnyPCA.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/TallSkinnySVD.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/mllib/Word2VecExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/pythonconverters/AvroConverters.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/sql/RDDRelation.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/sql/SQLDataSourceExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/sql/SparkSQLExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/sql/hive/SparkHiveExample.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/sql/streaming/StructuredNetworkWordCount.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/sql/streaming/StructuredNetworkWordCountWindowed.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/CustomReceiver.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/DirectKafkaWordCount.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/FlumeEventCount.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/FlumePollingEventCount.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/HdfsWordCount.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/KafkaWordCount.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/NetworkWordCount.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/QueueStream.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/RawNetworkGrep.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/RecoverableNetworkWordCount.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/SqlNetworkWordCount.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/StatefulNetworkWordCount.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/StreamingExamples.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/clickstream/PageViewGenerator.scala
/usr/share/apache-spark/examples/src/main/scala/org/apache/spark/examples/streaming/clickstream/PageViewStream.scala
/usr/share/apache-spark/examples/jars/scopt_2.11-3.3.0.jar
/usr/share/apache-spark/examples/jars/spark-examples_2.11-2.0.0.jar
/usr/share/apache-spark/jars/spark-catalyst_2.11.jar
/usr/share/apache-spark/jars/spark-core_2.11.jar
/usr/share/apache-spark/jars/spark-examples_2.11.jar
/usr/share/apache-spark/jars/spark-graphx_2.11.jar
/usr/share/apache-spark/jars/spark-hive_2.11.jar
/usr/share/apache-spark/jars/spark-launcher_2.11.jar
/usr/share/apache-spark/jars/spark-mllib-local_2.11.jar
/usr/share/apache-spark/jars/spark-mllib_2.11.jar
/usr/share/apache-spark/jars/spark-network-common_2.11.jar
/usr/share/apache-spark/jars/spark-network-shuffle_2.11.jar
/usr/share/apache-spark/jars/spark-repl_2.11.jar
/usr/share/apache-spark/jars/spark-sketch_2.11.jar
/usr/share/apache-spark/jars/spark-sql_2.11.jar
/usr/share/apache-spark/jars/spark-streaming-flume-assembly_2.11.jar
/usr/share/apache-spark/jars/spark-streaming-flume-sink_2.11.jar
/usr/share/apache-spark/jars/spark-streaming-flume_2.11.jar
/usr/share/apache-spark/jars/spark-streaming-kafka-0-10-assembly_2.11.jar
/usr/share/apache-spark/jars/spark-streaming-kafka-0-10_2.11.jar
/usr/share/apache-spark/jars/spark-streaming-kafka-0-8-assembly_2.11.jar
/usr/share/apache-spark/jars/spark-streaming-kafka-0-8_2.11.jar
/usr/share/apache-spark/jars/spark-streaming_2.11.jar
/usr/share/apache-spark/jars/spark-tags_2.11.jar
/usr/share/apache-spark/jars/spark-tools_2.11.jar
/usr/share/apache-spark/jars/spark-unsafe_2.11.jar
/usr/share/apache-spark/licenses/LICENSE-AnchorJS.txt
/usr/share/apache-spark/licenses/LICENSE-DPark.txt
/usr/share/apache-spark/licenses/LICENSE-Mockito.txt
/usr/share/apache-spark/licenses/LICENSE-SnapTree.txt
/usr/share/apache-spark/licenses/LICENSE-antlr.txt
/usr/share/apache-spark/licenses/LICENSE-boto.txt
/usr/share/apache-spark/licenses/LICENSE-cloudpickle.txt
/usr/share/apache-spark/licenses/LICENSE-d3.min.js.txt
/usr/share/apache-spark/licenses/LICENSE-dagre-d3.txt
/usr/share/apache-spark/licenses/LICENSE-f2j.txt
/usr/share/apache-spark/licenses/LICENSE-graphlib-dot.txt
/usr/share/apache-spark/licenses/LICENSE-heapq.txt
/usr/share/apache-spark/licenses/LICENSE-javolution.txt
/usr/share/apache-spark/licenses/LICENSE-jbcrypt.txt
/usr/share/apache-spark/licenses/LICENSE-jline.txt
/usr/share/apache-spark/licenses/LICENSE-jpmml-model.txt
/usr/share/apache-spark/licenses/LICENSE-jquery.txt
/usr/share/apache-spark/licenses/LICENSE-junit-interface.txt
/usr/share/apache-spark/licenses/LICENSE-kryo.txt
/usr/share/apache-spark/licenses/LICENSE-minlog.txt
/usr/share/apache-spark/licenses/LICENSE-modernizr.txt
/usr/share/apache-spark/licenses/LICENSE-netlib.txt
/usr/share/apache-spark/licenses/LICENSE-paranamer.txt
/usr/share/apache-spark/licenses/LICENSE-postgresql.txt
/usr/share/apache-spark/licenses/LICENSE-protobuf.txt
/usr/share/apache-spark/licenses/LICENSE-py4j.txt
/usr/share/apache-spark/licenses/LICENSE-pyrolite.txt
/usr/share/apache-spark/licenses/LICENSE-reflectasm.txt
/usr/share/apache-spark/licenses/LICENSE-sbt-launch-lib.txt
/usr/share/apache-spark/licenses/LICENSE-scala.txt
/usr/share/apache-spark/licenses/LICENSE-scalacheck.txt
/usr/share/apache-spark/licenses/LICENSE-scopt.txt
/usr/share/apache-spark/licenses/LICENSE-slf4j.txt
/usr/share/apache-spark/licenses/LICENSE-sorttable.js.txt
/usr/share/apache-spark/licenses/LICENSE-spire.txt
/usr/share/apache-spark/licenses/LICENSE-xmlenc.txt
/usr/share/apache-spark/python/.gitignore
/usr/share/apache-spark/python/docs/Makefile
/usr/share/apache-spark/python/docs/_static/pyspark.css
/usr/share/apache-spark/python/docs/_static/pyspark.js
/usr/share/apache-spark/python/docs/_templates/layout.html
/usr/share/apache-spark/python/docs/conf.py
/usr/share/apache-spark/python/docs/conf.pyc
/usr/share/apache-spark/python/docs/conf.pyo
/usr/share/apache-spark/python/docs/epytext.py
/usr/share/apache-spark/python/docs/epytext.pyc
/usr/share/apache-spark/python/docs/epytext.pyo
/usr/share/apache-spark/python/docs/index.rst
/usr/share/apache-spark/python/docs/make.bat
/usr/share/apache-spark/python/docs/make2.bat
/usr/share/apache-spark/python/docs/pyspark.ml.rst
/usr/share/apache-spark/python/docs/pyspark.mllib.rst
/usr/share/apache-spark/python/docs/pyspark.rst
/usr/share/apache-spark/python/docs/pyspark.sql.rst
/usr/share/apache-spark/python/docs/pyspark.streaming.rst
/usr/share/apache-spark/python/lib/PY4J_LICENSE.txt
/usr/share/apache-spark/python/lib/py4j-0.10.1-src.zip
/usr/share/apache-spark/python/lib/pyspark.zip
/usr/share/apache-spark/python/pylintrc
/usr/share/apache-spark/python/pyspark/__init__.py
/usr/share/apache-spark/python/pyspark/__init__.pyc
/usr/share/apache-spark/python/pyspark/__init__.pyo
/usr/share/apache-spark/python/pyspark/accumulators.py
/usr/share/apache-spark/python/pyspark/accumulators.pyc
/usr/share/apache-spark/python/pyspark/accumulators.pyo
/usr/share/apache-spark/python/pyspark/broadcast.py
/usr/share/apache-spark/python/pyspark/broadcast.pyc
/usr/share/apache-spark/python/pyspark/broadcast.pyo
/usr/share/apache-spark/python/pyspark/cloudpickle.py
/usr/share/apache-spark/python/pyspark/cloudpickle.pyc
/usr/share/apache-spark/python/pyspark/cloudpickle.pyo
/usr/share/apache-spark/python/pyspark/conf.py
/usr/share/apache-spark/python/pyspark/conf.pyc
/usr/share/apache-spark/python/pyspark/conf.pyo
/usr/share/apache-spark/python/pyspark/context.py
/usr/share/apache-spark/python/pyspark/context.pyc
/usr/share/apache-spark/python/pyspark/context.pyo
/usr/share/apache-spark/python/pyspark/daemon.py
/usr/share/apache-spark/python/pyspark/daemon.pyc
/usr/share/apache-spark/python/pyspark/daemon.pyo
/usr/share/apache-spark/python/pyspark/files.py
/usr/share/apache-spark/python/pyspark/files.pyc
/usr/share/apache-spark/python/pyspark/files.pyo
/usr/share/apache-spark/python/pyspark/heapq3.py
/usr/share/apache-spark/python/pyspark/heapq3.pyc
/usr/share/apache-spark/python/pyspark/heapq3.pyo
/usr/share/apache-spark/python/pyspark/java_gateway.py
/usr/share/apache-spark/python/pyspark/java_gateway.pyc
/usr/share/apache-spark/python/pyspark/java_gateway.pyo
/usr/share/apache-spark/python/pyspark/join.py
/usr/share/apache-spark/python/pyspark/join.pyc
/usr/share/apache-spark/python/pyspark/join.pyo
/usr/share/apache-spark/python/pyspark/ml/__init__.py
/usr/share/apache-spark/python/pyspark/ml/__init__.pyc
/usr/share/apache-spark/python/pyspark/ml/__init__.pyo
/usr/share/apache-spark/python/pyspark/ml/base.py
/usr/share/apache-spark/python/pyspark/ml/base.pyc
/usr/share/apache-spark/python/pyspark/ml/base.pyo
/usr/share/apache-spark/python/pyspark/ml/classification.py
/usr/share/apache-spark/python/pyspark/ml/classification.pyc
/usr/share/apache-spark/python/pyspark/ml/classification.pyo
/usr/share/apache-spark/python/pyspark/ml/clustering.py
/usr/share/apache-spark/python/pyspark/ml/clustering.pyc
/usr/share/apache-spark/python/pyspark/ml/clustering.pyo
/usr/share/apache-spark/python/pyspark/ml/common.py
/usr/share/apache-spark/python/pyspark/ml/common.pyc
/usr/share/apache-spark/python/pyspark/ml/common.pyo
/usr/share/apache-spark/python/pyspark/ml/evaluation.py
/usr/share/apache-spark/python/pyspark/ml/evaluation.pyc
/usr/share/apache-spark/python/pyspark/ml/evaluation.pyo
/usr/share/apache-spark/python/pyspark/ml/feature.py
/usr/share/apache-spark/python/pyspark/ml/feature.pyc
/usr/share/apache-spark/python/pyspark/ml/feature.pyo
/usr/share/apache-spark/python/pyspark/ml/linalg/__init__.py
/usr/share/apache-spark/python/pyspark/ml/linalg/__init__.pyc
/usr/share/apache-spark/python/pyspark/ml/linalg/__init__.pyo
/usr/share/apache-spark/python/pyspark/ml/param/__init__.py
/usr/share/apache-spark/python/pyspark/ml/param/__init__.pyc
/usr/share/apache-spark/python/pyspark/ml/param/__init__.pyo
/usr/share/apache-spark/python/pyspark/ml/param/_shared_params_code_gen.py
/usr/share/apache-spark/python/pyspark/ml/param/_shared_params_code_gen.pyc
/usr/share/apache-spark/python/pyspark/ml/param/_shared_params_code_gen.pyo
/usr/share/apache-spark/python/pyspark/ml/param/shared.py
/usr/share/apache-spark/python/pyspark/ml/param/shared.pyc
/usr/share/apache-spark/python/pyspark/ml/param/shared.pyo
/usr/share/apache-spark/python/pyspark/ml/pipeline.py
/usr/share/apache-spark/python/pyspark/ml/pipeline.pyc
/usr/share/apache-spark/python/pyspark/ml/pipeline.pyo
/usr/share/apache-spark/python/pyspark/ml/recommendation.py
/usr/share/apache-spark/python/pyspark/ml/recommendation.pyc
/usr/share/apache-spark/python/pyspark/ml/recommendation.pyo
/usr/share/apache-spark/python/pyspark/ml/regression.py
/usr/share/apache-spark/python/pyspark/ml/regression.pyc
/usr/share/apache-spark/python/pyspark/ml/regression.pyo
/usr/share/apache-spark/python/pyspark/ml/tests.py
/usr/share/apache-spark/python/pyspark/ml/tests.pyc
/usr/share/apache-spark/python/pyspark/ml/tests.pyo
/usr/share/apache-spark/python/pyspark/ml/tuning.py
/usr/share/apache-spark/python/pyspark/ml/tuning.pyc
/usr/share/apache-spark/python/pyspark/ml/tuning.pyo
/usr/share/apache-spark/python/pyspark/ml/util.py
/usr/share/apache-spark/python/pyspark/ml/util.pyc
/usr/share/apache-spark/python/pyspark/ml/util.pyo
/usr/share/apache-spark/python/pyspark/ml/wrapper.py
/usr/share/apache-spark/python/pyspark/ml/wrapper.pyc
/usr/share/apache-spark/python/pyspark/ml/wrapper.pyo
/usr/share/apache-spark/python/pyspark/mllib/__init__.py
/usr/share/apache-spark/python/pyspark/mllib/__init__.pyc
/usr/share/apache-spark/python/pyspark/mllib/__init__.pyo
/usr/share/apache-spark/python/pyspark/mllib/classification.py
/usr/share/apache-spark/python/pyspark/mllib/classification.pyc
/usr/share/apache-spark/python/pyspark/mllib/classification.pyo
/usr/share/apache-spark/python/pyspark/mllib/clustering.py
/usr/share/apache-spark/python/pyspark/mllib/clustering.pyc
/usr/share/apache-spark/python/pyspark/mllib/clustering.pyo
/usr/share/apache-spark/python/pyspark/mllib/common.py
/usr/share/apache-spark/python/pyspark/mllib/common.pyc
/usr/share/apache-spark/python/pyspark/mllib/common.pyo
/usr/share/apache-spark/python/pyspark/mllib/evaluation.py
/usr/share/apache-spark/python/pyspark/mllib/evaluation.pyc
/usr/share/apache-spark/python/pyspark/mllib/evaluation.pyo
/usr/share/apache-spark/python/pyspark/mllib/feature.py
/usr/share/apache-spark/python/pyspark/mllib/feature.pyc
/usr/share/apache-spark/python/pyspark/mllib/feature.pyo
/usr/share/apache-spark/python/pyspark/mllib/fpm.py
/usr/share/apache-spark/python/pyspark/mllib/fpm.pyc
/usr/share/apache-spark/python/pyspark/mllib/fpm.pyo
/usr/share/apache-spark/python/pyspark/mllib/linalg/__init__.py
/usr/share/apache-spark/python/pyspark/mllib/linalg/__init__.pyc
/usr/share/apache-spark/python/pyspark/mllib/linalg/__init__.pyo
/usr/share/apache-spark/python/pyspark/mllib/linalg/distributed.py
/usr/share/apache-spark/python/pyspark/mllib/linalg/distributed.pyc
/usr/share/apache-spark/python/pyspark/mllib/linalg/distributed.pyo
/usr/share/apache-spark/python/pyspark/mllib/random.py
/usr/share/apache-spark/python/pyspark/mllib/random.pyc
/usr/share/apache-spark/python/pyspark/mllib/random.pyo
/usr/share/apache-spark/python/pyspark/mllib/recommendation.py
/usr/share/apache-spark/python/pyspark/mllib/recommendation.pyc
/usr/share/apache-spark/python/pyspark/mllib/recommendation.pyo
/usr/share/apache-spark/python/pyspark/mllib/regression.py
/usr/share/apache-spark/python/pyspark/mllib/regression.pyc
/usr/share/apache-spark/python/pyspark/mllib/regression.pyo
/usr/share/apache-spark/python/pyspark/mllib/stat/KernelDensity.py
/usr/share/apache-spark/python/pyspark/mllib/stat/KernelDensity.pyc
/usr/share/apache-spark/python/pyspark/mllib/stat/KernelDensity.pyo
/usr/share/apache-spark/python/pyspark/mllib/stat/__init__.py
/usr/share/apache-spark/python/pyspark/mllib/stat/__init__.pyc
/usr/share/apache-spark/python/pyspark/mllib/stat/__init__.pyo
/usr/share/apache-spark/python/pyspark/mllib/stat/_statistics.py
/usr/share/apache-spark/python/pyspark/mllib/stat/_statistics.pyc
/usr/share/apache-spark/python/pyspark/mllib/stat/_statistics.pyo
/usr/share/apache-spark/python/pyspark/mllib/stat/distribution.py
/usr/share/apache-spark/python/pyspark/mllib/stat/distribution.pyc
/usr/share/apache-spark/python/pyspark/mllib/stat/distribution.pyo
/usr/share/apache-spark/python/pyspark/mllib/stat/test.py
/usr/share/apache-spark/python/pyspark/mllib/stat/test.pyc
/usr/share/apache-spark/python/pyspark/mllib/stat/test.pyo
/usr/share/apache-spark/python/pyspark/mllib/tests.py
/usr/share/apache-spark/python/pyspark/mllib/tests.pyc
/usr/share/apache-spark/python/pyspark/mllib/tests.pyo
/usr/share/apache-spark/python/pyspark/mllib/tree.py
/usr/share/apache-spark/python/pyspark/mllib/tree.pyc
/usr/share/apache-spark/python/pyspark/mllib/tree.pyo
/usr/share/apache-spark/python/pyspark/mllib/util.py
/usr/share/apache-spark/python/pyspark/mllib/util.pyc
/usr/share/apache-spark/python/pyspark/mllib/util.pyo
/usr/share/apache-spark/python/pyspark/profiler.py
/usr/share/apache-spark/python/pyspark/profiler.pyc
/usr/share/apache-spark/python/pyspark/profiler.pyo
/usr/share/apache-spark/python/pyspark/rdd.py
/usr/share/apache-spark/python/pyspark/rdd.pyc
/usr/share/apache-spark/python/pyspark/rdd.pyo
/usr/share/apache-spark/python/pyspark/rddsampler.py
/usr/share/apache-spark/python/pyspark/rddsampler.pyc
/usr/share/apache-spark/python/pyspark/rddsampler.pyo
/usr/share/apache-spark/python/pyspark/resultiterable.py
/usr/share/apache-spark/python/pyspark/resultiterable.pyc
/usr/share/apache-spark/python/pyspark/resultiterable.pyo
/usr/share/apache-spark/python/pyspark/serializers.py
/usr/share/apache-spark/python/pyspark/serializers.pyc
/usr/share/apache-spark/python/pyspark/serializers.pyo
/usr/share/apache-spark/python/pyspark/shell.py
/usr/share/apache-spark/python/pyspark/shell.pyc
/usr/share/apache-spark/python/pyspark/shell.pyo
/usr/share/apache-spark/python/pyspark/shuffle.py
/usr/share/apache-spark/python/pyspark/shuffle.pyc
/usr/share/apache-spark/python/pyspark/shuffle.pyo
/usr/share/apache-spark/python/pyspark/sql/__init__.py
/usr/share/apache-spark/python/pyspark/sql/__init__.pyc
/usr/share/apache-spark/python/pyspark/sql/__init__.pyo
/usr/share/apache-spark/python/pyspark/sql/catalog.py
/usr/share/apache-spark/python/pyspark/sql/catalog.pyc
/usr/share/apache-spark/python/pyspark/sql/catalog.pyo
/usr/share/apache-spark/python/pyspark/sql/column.py
/usr/share/apache-spark/python/pyspark/sql/column.pyc
/usr/share/apache-spark/python/pyspark/sql/column.pyo
/usr/share/apache-spark/python/pyspark/sql/conf.py
/usr/share/apache-spark/python/pyspark/sql/conf.pyc
/usr/share/apache-spark/python/pyspark/sql/conf.pyo
/usr/share/apache-spark/python/pyspark/sql/context.py
/usr/share/apache-spark/python/pyspark/sql/context.pyc
/usr/share/apache-spark/python/pyspark/sql/context.pyo
/usr/share/apache-spark/python/pyspark/sql/dataframe.py
/usr/share/apache-spark/python/pyspark/sql/dataframe.pyc
/usr/share/apache-spark/python/pyspark/sql/dataframe.pyo
/usr/share/apache-spark/python/pyspark/sql/functions.py
/usr/share/apache-spark/python/pyspark/sql/functions.pyc
/usr/share/apache-spark/python/pyspark/sql/functions.pyo
/usr/share/apache-spark/python/pyspark/sql/group.py
/usr/share/apache-spark/python/pyspark/sql/group.pyc
/usr/share/apache-spark/python/pyspark/sql/group.pyo
/usr/share/apache-spark/python/pyspark/sql/readwriter.py
/usr/share/apache-spark/python/pyspark/sql/readwriter.pyc
/usr/share/apache-spark/python/pyspark/sql/readwriter.pyo
/usr/share/apache-spark/python/pyspark/sql/session.py
/usr/share/apache-spark/python/pyspark/sql/session.pyc
/usr/share/apache-spark/python/pyspark/sql/session.pyo
/usr/share/apache-spark/python/pyspark/sql/streaming.py
/usr/share/apache-spark/python/pyspark/sql/streaming.pyc
/usr/share/apache-spark/python/pyspark/sql/streaming.pyo
/usr/share/apache-spark/python/pyspark/sql/tests.py
/usr/share/apache-spark/python/pyspark/sql/tests.pyc
/usr/share/apache-spark/python/pyspark/sql/tests.pyo
/usr/share/apache-spark/python/pyspark/sql/types.py
/usr/share/apache-spark/python/pyspark/sql/types.pyc
/usr/share/apache-spark/python/pyspark/sql/types.pyo
/usr/share/apache-spark/python/pyspark/sql/utils.py
/usr/share/apache-spark/python/pyspark/sql/utils.pyc
/usr/share/apache-spark/python/pyspark/sql/utils.pyo
/usr/share/apache-spark/python/pyspark/sql/window.py
/usr/share/apache-spark/python/pyspark/sql/window.pyc
/usr/share/apache-spark/python/pyspark/sql/window.pyo
/usr/share/apache-spark/python/pyspark/statcounter.py
/usr/share/apache-spark/python/pyspark/statcounter.pyc
/usr/share/apache-spark/python/pyspark/statcounter.pyo
/usr/share/apache-spark/python/pyspark/status.py
/usr/share/apache-spark/python/pyspark/status.pyc
/usr/share/apache-spark/python/pyspark/status.pyo
/usr/share/apache-spark/python/pyspark/storagelevel.py
/usr/share/apache-spark/python/pyspark/storagelevel.pyc
/usr/share/apache-spark/python/pyspark/storagelevel.pyo
/usr/share/apache-spark/python/pyspark/streaming/__init__.py
/usr/share/apache-spark/python/pyspark/streaming/__init__.pyc
/usr/share/apache-spark/python/pyspark/streaming/__init__.pyo
/usr/share/apache-spark/python/pyspark/streaming/context.py
/usr/share/apache-spark/python/pyspark/streaming/context.pyc
/usr/share/apache-spark/python/pyspark/streaming/context.pyo
/usr/share/apache-spark/python/pyspark/streaming/dstream.py
/usr/share/apache-spark/python/pyspark/streaming/dstream.pyc
/usr/share/apache-spark/python/pyspark/streaming/dstream.pyo
/usr/share/apache-spark/python/pyspark/streaming/flume.py
/usr/share/apache-spark/python/pyspark/streaming/flume.pyc
/usr/share/apache-spark/python/pyspark/streaming/flume.pyo
/usr/share/apache-spark/python/pyspark/streaming/kafka.py
/usr/share/apache-spark/python/pyspark/streaming/kafka.pyc
/usr/share/apache-spark/python/pyspark/streaming/kafka.pyo
/usr/share/apache-spark/python/pyspark/streaming/kinesis.py
/usr/share/apache-spark/python/pyspark/streaming/kinesis.pyc
/usr/share/apache-spark/python/pyspark/streaming/kinesis.pyo
/usr/share/apache-spark/python/pyspark/streaming/listener.py
/usr/share/apache-spark/python/pyspark/streaming/listener.pyc
/usr/share/apache-spark/python/pyspark/streaming/listener.pyo
/usr/share/apache-spark/python/pyspark/streaming/tests.py
/usr/share/apache-spark/python/pyspark/streaming/tests.pyc
/usr/share/apache-spark/python/pyspark/streaming/tests.pyo
/usr/share/apache-spark/python/pyspark/streaming/util.py
/usr/share/apache-spark/python/pyspark/streaming/util.pyc
/usr/share/apache-spark/python/pyspark/streaming/util.pyo
/usr/share/apache-spark/python/pyspark/tests.py
/usr/share/apache-spark/python/pyspark/tests.pyc
/usr/share/apache-spark/python/pyspark/tests.pyo
/usr/share/apache-spark/python/pyspark/traceback_utils.py
/usr/share/apache-spark/python/pyspark/traceback_utils.pyc
/usr/share/apache-spark/python/pyspark/traceback_utils.pyo
/usr/share/apache-spark/python/pyspark/worker.py
/usr/share/apache-spark/python/pyspark/worker.pyc
/usr/share/apache-spark/python/pyspark/worker.pyo
/usr/share/apache-spark/python/run-tests
/usr/share/apache-spark/python/run-tests.py
/usr/share/apache-spark/python/run-tests.pyc
/usr/share/apache-spark/python/run-tests.pyo
/usr/share/apache-spark/python/test_support/SimpleHTTPServer.py
/usr/share/apache-spark/python/test_support/SimpleHTTPServer.pyc
/usr/share/apache-spark/python/test_support/SimpleHTTPServer.pyo
/usr/share/apache-spark/python/test_support/hello.txt
/usr/share/apache-spark/python/test_support/sql/ages.csv
/usr/share/apache-spark/python/test_support/sql/orc_partitioned/_SUCCESS
/usr/share/apache-spark/python/test_support/sql/orc_partitioned/b=0/c=0/.part-r-00000-829af031-b970-49d6-ad39-30460a0be2c8.orc.crc
/usr/share/apache-spark/python/test_support/sql/orc_partitioned/b=0/c=0/part-r-00000-829af031-b970-49d6-ad39-30460a0be2c8.orc
/usr/share/apache-spark/python/test_support/sql/orc_partitioned/b=1/c=1/.part-r-00000-829af031-b970-49d6-ad39-30460a0be2c8.orc.crc
/usr/share/apache-spark/python/test_support/sql/orc_partitioned/b=1/c=1/part-r-00000-829af031-b970-49d6-ad39-30460a0be2c8.orc
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/_SUCCESS
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/_common_metadata
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/_metadata
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/year=2014/month=9/day=1/.part-r-00008.gz.parquet.crc
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/year=2014/month=9/day=1/part-r-00008.gz.parquet
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/year=2015/month=10/day=25/.part-r-00002.gz.parquet.crc
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/year=2015/month=10/day=25/.part-r-00004.gz.parquet.crc
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/year=2015/month=10/day=25/part-r-00002.gz.parquet
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/year=2015/month=10/day=25/part-r-00004.gz.parquet
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/year=2015/month=10/day=26/.part-r-00005.gz.parquet.crc
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/year=2015/month=10/day=26/part-r-00005.gz.parquet
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/year=2015/month=9/day=1/.part-r-00007.gz.parquet.crc
/usr/share/apache-spark/python/test_support/sql/parquet_partitioned/year=2015/month=9/day=1/part-r-00007.gz.parquet
/usr/share/apache-spark/python/test_support/sql/people.json
/usr/share/apache-spark/python/test_support/sql/people1.json
/usr/share/apache-spark/python/test_support/sql/streaming/text-test.txt
/usr/share/apache-spark/python/test_support/sql/text-test.txt
/usr/share/apache-spark/python/test_support/userlib-0.1.zip
/usr/share/apache-spark/python/test_support/userlibrary.py
/usr/share/apache-spark/python/test_support/userlibrary.pyc
/usr/share/apache-spark/python/test_support/userlibrary.pyo
/usr/share/apache-spark/sbin/slaves.sh
/usr/share/apache-spark/sbin/spark-config.sh
/usr/share/apache-spark/sbin/spark-daemon.sh
/usr/share/apache-spark/sbin/spark-daemons.sh
/usr/share/apache-spark/sbin/start-all.sh
/usr/share/apache-spark/sbin/start-history-server.sh
/usr/share/apache-spark/sbin/start-master.sh
/usr/share/apache-spark/sbin/start-mesos-dispatcher.sh
/usr/share/apache-spark/sbin/start-mesos-shuffle-service.sh
/usr/share/apache-spark/sbin/start-shuffle-service.sh
/usr/share/apache-spark/sbin/start-slave.sh
/usr/share/apache-spark/sbin/start-slaves.sh
/usr/share/apache-spark/sbin/start-thriftserver.sh
/usr/share/apache-spark/sbin/stop-all.sh
/usr/share/apache-spark/sbin/stop-history-server.sh
/usr/share/apache-spark/sbin/stop-master.sh
/usr/share/apache-spark/sbin/stop-mesos-dispatcher.sh
/usr/share/apache-spark/sbin/stop-mesos-shuffle-service.sh
/usr/share/apache-spark/sbin/stop-shuffle-service.sh
/usr/share/apache-spark/sbin/stop-slave.sh
/usr/share/apache-spark/sbin/stop-slaves.sh
/usr/share/apache-spark/sbin/stop-thriftserver.sh
/usr/share/apache-spark/yarn/pom.xml
/usr/share/apache-spark/yarn/src/main/resources/META-INF/services/org.apache.spark.scheduler.ExternalClusterManager
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/AMDelegationTokenRenewer.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/ApplicationMaster.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/ApplicationMasterArguments.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/Client.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/ClientArguments.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/ClientDistributedCacheManager.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/ExecutorDelegationTokenUpdater.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/ExecutorRunnable.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/LocalityPreferredContainerPlacementStrategy.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/YarnAllocator.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/YarnRMClient.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/YarnSparkHadoopUtil.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/deploy/yarn/config.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/launcher/YarnCommandBuilderUtils.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/scheduler/cluster/SchedulerExtensionService.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/scheduler/cluster/YarnClientSchedulerBackend.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/scheduler/cluster/YarnClusterManager.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/scheduler/cluster/YarnClusterScheduler.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/scheduler/cluster/YarnClusterSchedulerBackend.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/scheduler/cluster/YarnScheduler.scala
/usr/share/apache-spark/yarn/src/main/scala/org/apache/spark/scheduler/cluster/YarnSchedulerBackend.scala
/usr/share/apache-spark/yarn/src/test/resources/log4j.properties
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/deploy/yarn/BaseYarnClusterSuite.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/deploy/yarn/ClientDistributedCacheManagerSuite.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/deploy/yarn/ClientSuite.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/deploy/yarn/ContainerPlacementStrategySuite.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/deploy/yarn/YarnAllocatorSuite.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/deploy/yarn/YarnClusterSuite.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/deploy/yarn/YarnShuffleIntegrationSuite.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/deploy/yarn/YarnSparkHadoopUtilSuite.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/launcher/TestClasspathBuilder.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/network/shuffle/ShuffleTestAccessor.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/network/yarn/YarnShuffleServiceSuite.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/network/yarn/YarnTestAccessor.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/scheduler/cluster/ExtensionServiceIntegrationSuite.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/scheduler/cluster/SimpleExtensionService.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/scheduler/cluster/StubApplicationAttemptId.scala
/usr/share/apache-spark/yarn/src/test/scala/org/apache/spark/scheduler/cluster/StubApplicationId.scala
/usr/share/java/spark/spark-catalyst_2.11.jar
/usr/share/java/spark/spark-core_2.11.jar
/usr/share/java/spark/spark-examples_2.11.jar
/usr/share/java/spark/spark-graphx_2.11.jar
/usr/share/java/spark/spark-hive_2.11.jar
/usr/share/java/spark/spark-launcher_2.11.jar
/usr/share/java/spark/spark-mllib-local_2.11.jar
/usr/share/java/spark/spark-mllib_2.11.jar
/usr/share/java/spark/spark-network-common_2.11.jar
/usr/share/java/spark/spark-network-shuffle_2.11.jar
/usr/share/java/spark/spark-repl_2.11.jar
/usr/share/java/spark/spark-sketch_2.11.jar
/usr/share/java/spark/spark-sql_2.11.jar
/usr/share/java/spark/spark-streaming-flume-assembly_2.11.jar
/usr/share/java/spark/spark-streaming-flume-sink_2.11.jar
/usr/share/java/spark/spark-streaming-flume_2.11.jar
/usr/share/java/spark/spark-streaming-kafka-0-10-assembly_2.11.jar
/usr/share/java/spark/spark-streaming-kafka-0-10_2.11.jar
/usr/share/java/spark/spark-streaming-kafka-0-8-assembly_2.11.jar
/usr/share/java/spark/spark-streaming-kafka-0-8_2.11.jar
/usr/share/java/spark/spark-streaming_2.11.jar
/usr/share/java/spark/spark-tags_2.11.jar
/usr/share/java/spark/spark-tools_2.11.jar
/usr/share/java/spark/spark-unsafe_2.11.jar
/usr/share/maven-metadata/apache-spark.xml
/usr/share/maven-poms/apache-spark/java8-tests_2.11.pom
/usr/share/maven-poms/apache-spark/spark-assembly_2.11.pom
/usr/share/maven-poms/apache-spark/spark-catalyst_2.11.pom
/usr/share/maven-poms/apache-spark/spark-core_2.11.pom
/usr/share/maven-poms/apache-spark/spark-examples_2.11.pom
/usr/share/maven-poms/apache-spark/spark-graphx_2.11.pom
/usr/share/maven-poms/apache-spark/spark-hive_2.11.pom
/usr/share/maven-poms/apache-spark/spark-launcher_2.11.pom
/usr/share/maven-poms/apache-spark/spark-mllib-local_2.11.pom
/usr/share/maven-poms/apache-spark/spark-mllib_2.11.pom
/usr/share/maven-poms/apache-spark/spark-network-common_2.11.pom
/usr/share/maven-poms/apache-spark/spark-network-shuffle_2.11.pom
/usr/share/maven-poms/apache-spark/spark-parent_2.11.pom
/usr/share/maven-poms/apache-spark/spark-repl_2.11.pom
/usr/share/maven-poms/apache-spark/spark-sketch_2.11.pom
/usr/share/maven-poms/apache-spark/spark-sql_2.11.pom
/usr/share/maven-poms/apache-spark/spark-streaming-flume-assembly_2.11.pom
/usr/share/maven-poms/apache-spark/spark-streaming-flume-sink_2.11.pom
/usr/share/maven-poms/apache-spark/spark-streaming-flume_2.11.pom
/usr/share/maven-poms/apache-spark/spark-streaming-kafka-0-10-assembly_2.11.pom
/usr/share/maven-poms/apache-spark/spark-streaming-kafka-0-10_2.11.pom
/usr/share/maven-poms/apache-spark/spark-streaming-kafka-0-8-assembly_2.11.pom
/usr/share/maven-poms/apache-spark/spark-streaming-kafka-0-8_2.11.pom
/usr/share/maven-poms/apache-spark/spark-streaming_2.11.pom
/usr/share/maven-poms/apache-spark/spark-tags_2.11.pom
/usr/share/maven-poms/apache-spark/spark-tools_2.11.pom
/usr/share/maven-poms/apache-spark/spark-unsafe_2.11.pom
/usr/share/apache-spark/jars/RoaringBitmap-0.5.11.jar
/usr/share/apache-spark/jars/antlr4-runtime-4.5.3.jar
/usr/share/apache-spark/jars/aopalliance-1.0.jar
/usr/share/apache-spark/jars/arpack_combined_all-0.1.jar
/usr/share/apache-spark/jars/avro-1.7.7.jar
/usr/share/apache-spark/jars/avro-ipc-1.7.7.jar
/usr/share/apache-spark/jars/avro-mapred-1.7.7-hadoop2.jar
/usr/share/apache-spark/jars/breeze-macros_2.11-0.11.2.jar
/usr/share/apache-spark/jars/breeze_2.11-0.11.2.jar
/usr/share/apache-spark/jars/chill-java-0.8.0.jar
/usr/share/apache-spark/jars/chill_2.11-0.8.0.jar
/usr/share/apache-spark/jars/commons-beanutils-1.8.3.jar
/usr/share/apache-spark/jars/commons-beanutils-core-1.8.0.jar
/usr/share/apache-spark/jars/commons-cli-1.2.jar
/usr/share/apache-spark/jars/commons-codec-1.10.jar
/usr/share/apache-spark/jars/commons-collections-3.2.2.jar
/usr/share/apache-spark/jars/commons-compiler-2.7.8.jar
/usr/share/apache-spark/jars/commons-compress-1.4.1.jar
/usr/share/apache-spark/jars/commons-configuration-1.6.jar
/usr/share/apache-spark/jars/commons-digester-1.8.jar
/usr/share/apache-spark/jars/commons-httpclient-3.1.jar
/usr/share/apache-spark/jars/commons-io-2.4.jar
/usr/share/apache-spark/jars/commons-lang-2.6.jar
/usr/share/apache-spark/jars/commons-lang3-3.3.2.jar
/usr/share/apache-spark/jars/commons-logging-1.2.jar
/usr/share/apache-spark/jars/commons-math-2.1.jar
/usr/share/apache-spark/jars/commons-math3-3.4.1.jar
/usr/share/apache-spark/jars/commons-net-2.2.jar
/usr/share/apache-spark/jars/compress-lzf-1.0.3.jar
/usr/share/apache-spark/jars/core-1.1.2.jar
/usr/share/apache-spark/jars/cssparser-0.9.16.jar
/usr/share/apache-spark/jars/curator-client-2.4.0.jar
/usr/share/apache-spark/jars/curator-framework-2.4.0.jar
/usr/share/apache-spark/jars/curator-recipes-2.4.0.jar
/usr/share/apache-spark/jars/guava-14.0.1.jar
/usr/share/apache-spark/jars/guice-3.0.jar
/usr/share/apache-spark/jars/hadoop-annotations-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-auth-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-client-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-common-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-hdfs-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-mapreduce-client-app-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-mapreduce-client-common-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-mapreduce-client-core-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-mapreduce-client-jobclient-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-mapreduce-client-shuffle-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-yarn-api-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-yarn-client-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-yarn-common-2.2.0.jar
/usr/share/apache-spark/jars/hadoop-yarn-server-common-2.2.0.jar
/usr/share/apache-spark/jars/htmlunit-2.18.jar
/usr/share/apache-spark/jars/htmlunit-core-js-2.17.jar
/usr/share/apache-spark/jars/httpclient-4.5.2.jar
/usr/share/apache-spark/jars/httpcore-4.4.4.jar
/usr/share/apache-spark/jars/httpmime-4.5.2.jar
/usr/share/apache-spark/jars/ivy-2.4.0.jar
/usr/share/apache-spark/jars/jackson-annotations-2.6.5.jar
/usr/share/apache-spark/jars/jackson-core-2.5.0.jar
/usr/share/apache-spark/jars/jackson-core-asl-1.9.13.jar
/usr/share/apache-spark/jars/jackson-databind-2.6.5.jar
/usr/share/apache-spark/jars/jackson-mapper-asl-1.9.13.jar
/usr/share/apache-spark/jars/jackson-module-paranamer-2.6.5.jar
/usr/share/apache-spark/jars/jackson-module-scala_2.11-2.6.5.jar
/usr/share/apache-spark/jars/janino-2.7.8.jar
/usr/share/apache-spark/jars/javax.inject-1.jar
/usr/share/apache-spark/jars/javax.servlet-api-3.1.0.jar
/usr/share/apache-spark/jars/javax.ws.rs-api-2.0.1.jar
/usr/share/apache-spark/jars/jcl-over-slf4j-1.7.16.jar
/usr/share/apache-spark/jars/jersey-client-2.22.2.jar
/usr/share/apache-spark/jars/jersey-common-2.22.2.jar
/usr/share/apache-spark/jars/jersey-container-servlet-2.22.2.jar
/usr/share/apache-spark/jars/jersey-container-servlet-core-2.22.2.jar
/usr/share/apache-spark/jars/jersey-server-2.22.2.jar
/usr/share/apache-spark/jars/jets3t-0.7.1.jar
/usr/share/apache-spark/jars/jetty-io-9.3.0.v20150612.jar
/usr/share/apache-spark/jars/jetty-util-6.1.26.jar
/usr/share/apache-spark/jars/json4s-ast_2.11-3.2.11.jar
/usr/share/apache-spark/jars/json4s-core_2.11-3.2.11.jar
/usr/share/apache-spark/jars/json4s-jackson_2.11-3.2.11.jar
/usr/share/apache-spark/jars/jsr305-1.3.9.jar
/usr/share/apache-spark/jars/jtransforms-2.4.0.jar
/usr/share/apache-spark/jars/jul-to-slf4j-1.7.16.jar
/usr/share/apache-spark/jars/kryo-shaded-3.0.3.jar
/usr/share/apache-spark/jars/leveldb-SYSTEM.jar
/usr/share/apache-spark/jars/leveldb-api-SYSTEM.jar
/usr/share/apache-spark/jars/leveldbjni-all-1.8.jar
/usr/share/apache-spark/jars/log4j-1.2.17.jar
/usr/share/apache-spark/jars/lz4-1.3.0.jar
/usr/share/apache-spark/jars/mesos-0.21.1-shaded-protobuf.jar
/usr/share/apache-spark/jars/metrics-core-3.1.2.jar
/usr/share/apache-spark/jars/metrics-graphite-3.1.2.jar
/usr/share/apache-spark/jars/metrics-json-3.1.2.jar
/usr/share/apache-spark/jars/metrics-jvm-3.1.2.jar
/usr/share/apache-spark/jars/minlog-1.3.0.jar
/usr/share/apache-spark/jars/nekohtml-1.9.22.jar
/usr/share/apache-spark/jars/netty-3.8.0.Final.jar
/usr/share/apache-spark/jars/netty-all-4.0.29.Final.jar
/usr/share/apache-spark/jars/objenesis-2.1.jar
/usr/share/apache-spark/jars/opencsv-2.3.jar
/usr/share/apache-spark/jars/oro-2.0.8.jar
/usr/share/apache-spark/jars/paranamer-2.6.jar
/usr/share/apache-spark/jars/parquet-column-1.7.0.jar
/usr/share/apache-spark/jars/parquet-common-1.7.0.jar
/usr/share/apache-spark/jars/parquet-encoding-1.7.0.jar
/usr/share/apache-spark/jars/parquet-format-2.3.0-incubating.jar
/usr/share/apache-spark/jars/parquet-generator-1.7.0.jar
/usr/share/apache-spark/jars/parquet-hadoop-1.7.0.jar
/usr/share/apache-spark/jars/parquet-jackson-1.7.0.jar
/usr/share/apache-spark/jars/pmml-model-1.2.15.jar
/usr/share/apache-spark/jars/protobuf-java-2.5.0.jar
/usr/share/apache-spark/jars/py4j-0.10.1.jar
/usr/share/apache-spark/jars/pyrolite-4.9.jar
/usr/share/apache-spark/jars/sac-1.3.jar
/usr/share/apache-spark/jars/scala-compiler-2.11.8.jar
/usr/share/apache-spark/jars/scala-library-2.11.8.jar
/usr/share/apache-spark/jars/scala-parser-combinators_2.11-1.0.4.jar
/usr/share/apache-spark/jars/scala-reflect-2.11.8.jar
/usr/share/apache-spark/jars/scala-xml_2.11-1.0.2.jar
/usr/share/apache-spark/jars/scalap-2.11.8.jar
/usr/share/apache-spark/jars/serializer-2.7.1.jar
/usr/share/apache-spark/jars/slf4j-api-1.7.16.jar
/usr/share/apache-spark/jars/slf4j-log4j12-1.7.16.jar
/usr/share/apache-spark/jars/snappy-java-1.1.2.4.jar
/usr/share/apache-spark/jars/spire-macros_2.11-0.7.4.jar
/usr/share/apache-spark/jars/spire_2.11-0.7.4.jar
/usr/share/apache-spark/jars/stream-2.7.0.jar
/usr/share/apache-spark/jars/univocity-parsers-2.1.1.jar
/usr/share/apache-spark/jars/websocket-api-9.3.0.v20150612.jar
/usr/share/apache-spark/jars/websocket-client-9.2.12.v20150709.jar
/usr/share/apache-spark/jars/websocket-common-9.3.0.v20150612.jar
/usr/share/apache-spark/jars/xalan-2.7.2.jar
/usr/share/apache-spark/jars/xbean-asm5-shaded-4.4.jar
/usr/share/apache-spark/jars/xercesImpl-2.11.0.jar
/usr/share/apache-spark/jars/xmlenc-0.52.jar
/usr/share/apache-spark/jars/zookeeper-3.4.5.jar
