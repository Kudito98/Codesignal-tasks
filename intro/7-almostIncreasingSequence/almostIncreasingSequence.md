<p>Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.</p>
<p><em>Note:</em> sequence <code>a<sub>0</sub></code>, <code>a<sub>1</sub></code>, ..., <code>a<sub>n</sub></code> is considered to be a strictly increasing if <code>a<sub>0</sub> &lt; a<sub>1</sub> &lt; ... &lt; a<sub>n</sub></code>. Sequence containing only one element is also considered to be strictly increasing.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>sequence = [1, 3, 2, 1]</code>, the output should be<br />
<code>solution(sequence) = false</code>.</p>
<p>There is no one element in this array that can be removed in order to get a strictly increasing sequence.</p>
</li>
<li>
<p>For <code>sequence = [1, 3, 2]</code>, the output should be<br />
<code>solution(sequence) = true</code>.</p>
<p>You can remove <code>3</code> from the array to get the strictly increasing sequence <code>[1, 2]</code>. Alternately, you can remove <code>2</code> to get the strictly increasing sequence <code>[1, 3]</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer sequence</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ sequence.length ≤ 10<sup>5</sup></code>,<br />
<code>-10<sup>5</sup> ≤ sequence[i] ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p>Return <code>true</code> if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return <code>false</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
