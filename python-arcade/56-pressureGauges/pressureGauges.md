<p>Harry dropped out of school to pursue his dreams and work in Pipes Corporations. He is now in charge of a lot of pipes, and his task is to check the gauges twice a day. By analyzing the <code>morning</code> and <code>evening</code> pressures of each pipe, Harry should write a report about the minimum and the maximum pressure during the day.</p>
<p>Given the pressures Harry wrote down for each pipe, return two lists: the first one containing the minimum, and the second one containing the maximum pressure of each pipe during the day.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>morning = [3, 5, 2, 6]</code> and <code>evening = [1, 6, 6, 6]</code>,<br />
the output should be<br />
<code>solution(morning, evening) = [[1, 5, 2, 6], [3, 6, 6, 6]]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer morning</strong></p>
<p>A list of pressures, where the <code>i<sup>th</sup></code> element is the value the pressure gauge showed for the <code>i<sup>th</sup></code> pipe in the morning.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ morning.length ≤ 10</code>,<br />
<code>0 ≤ morning[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] array.integer evening</strong></p>
<p>A list of evening pressures in the same format as <code>morning</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>evening.length = morning.length</code>,<br />
<code>0 ≤ evening[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>A list containing two lists, where the <code>i<sup>th</sup></code> elements of the first and the second lists are the minimum and the maximum pressures the <code>i<sup>th</sup></code> pipe had, respectively.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
