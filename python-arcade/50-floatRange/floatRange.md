<p>As you may know, the <code>range</code> function in Python allows coders to iterate over elements from <code>start</code> to <code>stop</code> with the given <code>step</code>. Unfortunately it works only for integer values, and additional libraries should be used if a programmer wants to use float values.</p>
<p>CodeSignal doesn't include third-party libraries, so you have to make do with the standard ones. Given float numbers <code>start</code>, <code>stop</code> and <code>step</code>, your task is to return a list of values from <code>start</code> to <code>stop</code> (including <code>start</code> and not including <code>stop</code>), evenly spaced by the <code>step</code>.</p>
<p>Values <code>start</code>, <code>stop</code> and <code>step</code> have at most <code>5</code> digits after the decimal point each.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>start = -0.9</code>, <code>stop = 0.45</code>, and <code>step = 0.2</code>,<br />
the output should be<br />
<code>solution(start, stop, step) = [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] float start</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>-1000 ≤ start ≤ stop ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] float stop</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>-1000 ≤ start ≤ stop ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] float step</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>0.05 ≤ step ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.float</strong></p>
<p>A list of values in range <code>[start, stop)</code>, spaced by the <code>step</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
