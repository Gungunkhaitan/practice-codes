// CH.EN.U4CSE22074
package com.mapreduceproject;
import java.io.IOException;

public class WordCount Reducer extends Reducer<Text, IntWritable, Text, IntWritable>
    private IntWritable count = new IntWritable();

    public void reduce (Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException{ 
        int valueSum = 0;
        for (IntWritable val values)
        {
            valuesum += val.get();
        }

        count.set(valueSum);
        context.write(key, count);
        }
}