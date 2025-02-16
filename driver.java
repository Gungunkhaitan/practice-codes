// CH.EN.U4CSE22074
package com.mapreduceproject;
import org.apache.hadoop.conf.Configuration; 3 import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class WordCount {
    public static void main(String[] args) throws Exception {
        Configuration conf= new Configuration();
        String[] pathArgs = new GenericOptionsParser(conf, args).getRemainingArgs(); 
        if (pathArgs.length < 2) {
            System.err.println("MR Project Usage: wordcount <input-path> [...] <butput-path"); 
            System.exit(2);
        }
        Job wc Job Job.getInstance(conf, "MapReduce WordCount"); 
        wcJob.setJarByClass (WordCount.class);
        wcJob.setMapperclass (WordCountMapper.class);
        wcJob.setCombinerClass (WordCountReducer.class);
        wcJob.setReducerClass (WordCountReducer.class);

        wcJob.setOutputKeyClass(Text.class); 
        wcJob.setOutputValueClass(IntWritable.class);
        
        for (int i = 0; i < pathArgs.length - 1; ++i) {
            FileInputFormat.addInputPath(wc Job, new Path(pathArgs[i]));
        }

        FileOutputFormat.setOutputPath(wc Job, new Path(pathArgs [pathArgs.length - 1]));

        System.exit(wc Job.waitForCompletion (true) ? 0 : 1);

        }
}

