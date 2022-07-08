<p><code>N</code> candles are placed in a row, some of them are initially lit. For each candle from the <code>1st</code> to the <code>Nth</code> the following algorithm is applied: if the observed candle is lit then states of this candle and all candles before it are changed to the opposite. Which candles will remain lit after applying the algorithm to all candles in the order they are placed in the line?</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>a = [1, 1, 1, 1, 1]</code>, the output should be<br />
<code>solution(a) = [0, 1, 0, 1, 0]</code>.</p>
<p>Check out the image below for better understanding:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/switchLights/img/example.png?_tm=1624667826990" alt /></p>
</li>
<li>
<p>For <code>a = [0, 0]</code>, the output should be<br />
<code>solution(a) = [0, 0]</code>.</p>
<p>The candles are not initially lit, so their states are not altered by the algorithm.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer a</strong></p>
<p>Initial situation - array of zeros and ones of length <code>N</code>, <code>1</code> means that the corresponding candle is lit.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ a.length ≤ 5000</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Situation after applying the algorithm - array in the same format as input with the same length.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
