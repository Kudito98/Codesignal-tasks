<p>You've launched a revolutionary service not long ago, and were busy improving it for the last couple of months. When you finally decided that the service is perfect, you remembered that you created a feedbacks page long time ago, which you never checked out since then. Now that you have nothing left to do, you would like to have a look at what the community thinks of your service.</p>
<p>Unfortunately it looks like the feedbacks page is far from perfect: each <code>feedback</code> is displayed as a one-line string, and if it's too long there's no way to see what it is about. Naturally, this horrible bug should be fixed. Implement a function that, given a <code>feedback</code> and the <code>size</code> of the screen, splits the <code>feedback</code> into lines so that:</p>
<ul>
<li>each token (i.e. sequence of non-whitespace characters) belongs to one of the lines entirely;</li>
<li>each line is at most <code>size</code> characters long;</li>
<li>no line has trailing or leading spaces;</li>
<li>each line should have the maximum possible length, assuming that all lines before it were also the longest possible.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>feedback = "This is an example feedback"</code> and <code>size = 8</code>,<br />
the output should be</p>
<pre><code>solution(feedback, size) = ["This is", 
                                  "an", 
                                  "example", 
                                  "feedback"]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string feedback</strong></p>
<p>A string containing a feedback. Each feedback is guaranteed to contain only letters, punctuation marks and whitespace characters (<code>' '</code>).</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ feedback.length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[input] integer size</strong></p>
<p>The size of the screen. It is guaranteed that it is not smaller than the longest token in the <code>feedback</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ size ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>Lines from the <code>feedback</code>, split as described above.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
