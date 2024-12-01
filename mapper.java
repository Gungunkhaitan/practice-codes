// CH.EN.U4CSE22074
package com.mapreduceproject;
import java.io.IOException;

public class WordCountMapper extends Mapper<Longwritable, Text, Text, IntWritable>
    private final Text wordToken = new Text();
    public void map (LongWritable key, Text value, Context context) throws IOException, InterruptedException { 
        StringTokenizer tokens = new StringTokenizer (value.toString());
        while(tokens.hasMoreTokens())
        {
            wordToken.set(tokens.nextToken());
            context.write(wordToken, new IntWritable(1));

        }

    }
}
