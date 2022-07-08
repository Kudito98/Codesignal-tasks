<p>Given an array of <code>2<sup>k</sup></code> integers (for some integer <code>k</code>), perform the following operations until the array contains only one element:</p>
<ul>
<li>On the <code>1<sup>st</sup></code>, <code>3<sup>rd</sup></code>, <code>5<sup>th</sup></code>, etc. iterations (1-based) replace each pair of consecutive elements with their sum;</li>
<li>On the <code>2<sup>nd</sup></code>, <code>4<sup>th</sup></code>, <code>6<sup>th</sup></code>, etc. iterations replace each pair of consecutive elements with their product.</li>
</ul>
<p>After the algorithm has finished, there will be a single element left in the array. Return that element.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>inputArray = [1, 2, 3, 4, 5, 6, 7, 8]</code>, the output should be<br />
<code>solution(inputArray) = 186</code>.</p>
<p>We have <code>[1, 2, 3, 4, 5, 6, 7, 8] -&gt; [3, 7, 11, 15] -&gt; [21, 165] -&gt; [186]</code>, so the answer is <code>186</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer inputArray</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ inputArray.length ≤ 2<sup>7</sup></code>,<br />
<code>-100 ≤ inputArray[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
