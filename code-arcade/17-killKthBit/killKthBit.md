<p>In order to stop the Mad Coder evil genius you need to decipher the encrypted message he sent to his minions. The message contains several numbers that, when typed into a supercomputer, will launch a missile into the sky blocking out the sun, and making all the people on Earth grumpy and sad.</p>
<p>You figured out that some numbers have a modified single digit in their binary representation. More specifically, in the given number <code>n</code> the <code>k<sup>th</sup></code> bit from the right was initially set to <code>0</code>, but its current value might be different. It's now up to you to write a function that will change the <code>k<sup>th</sup></code> bit of <code>n</code> back to <code>0</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>n = 37</code> and <code>k = 3</code>, the output should be<br />
<code>solution(n, k) = 33</code>.</p>
<p><code>37<sub>10</sub> = 100<b><font color="red">1</font></b>01<sub>2</sub> ~&gt; 100<b><font color="red">0</font></b>01<sub>2</sub> = 33<sub>10</sub></code>.</p>
</li>
<li>
<p>For <code>n = 37</code> and <code>k = 4</code>, the output should be<br />
<code>solution(n, k) = 37</code>.</p>
<p>The <code>4<sup>th</sup></code> bit is <code>0</code> already (looks like the Mad Coder forgot to encrypt this number), so the answer is still <code>37</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ n ≤ 2<sup>31</sup> - 1</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p>The <code>1</code>-based index of the changed bit (counting from the right).</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ k ≤ 31</code>.</p>
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
