<p>No time to explain! The World Government made contact with intelligent alien life, and needs you to send a message to the outer space. The aliens only receive messages that are stored in a sequence of lists of sizes <code>0, 1, 1, 2, 3, 5, ...</code>, in other words those whose length increase according to the <a href="keyword://fibonacci-sequence" target="_blank">Fibonacci sequence</a>.</p>
<p>The Government is too busy composing the message, and needs you to prepare the list in which the message should be sent. Given an integer <code>n</code>, return a list of <code>n</code> lists, where the first element consists is empty (consists of <code>0</code> zeros), the second element consists of <code>1</code> zero, and so on.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>n = 6</code>, the output should be</p>
<pre><code>solution(n) = [[], 
                    [0], 
                    [0], 
                    [0, 0], 
                    [0, 0, 0], 
                    [0, 0, 0, 0, 0]]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The size of the list you should return.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ n ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>A 2-dimensional list of zeros, where the list sizes form the Fibonacci sequence.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
