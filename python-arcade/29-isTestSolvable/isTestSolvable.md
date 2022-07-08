<p>You've been preparing all night for the upcoming test and entered the class certain that you will ace it. Now that you received the test questions, you died inside a little: looks like you prepared for the test on a completely different topic.</p>
<p>You're not even sure if you should bother to answer the questions. You still have some hope though: it is known that there's a glitch in the test preparing system, so that if the sum of digits of question ids is divisible by <code>k</code>, the answer to each question has a <code>90%</code> probability to be an A.</p>
<p>Given the list of question <code>ids</code>, determine if the sum of their digits is divisible by <code>k</code> to see if it's worth trying to pass the test.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>ids = [529665, 909767, 644200]</code> and <code>k = 3</code>, the output should be<br />
<code>solution(ids, k) = true</code>.</p>
<p>The sum of digits is</p>
<pre><code>(5 + 2 + 9 + 6 + 6 + 5) + (9 + 0 + 9 + 7 + 6 + 7) + (6 + 4 + 4 + 2 + 0 + 0) = 87
</code></pre>
<p>which is divisible by <code>3</code>. Today is your lucky day after all!</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer ids</strong></p>
<p>Array of unique question ids.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ ids.length ≤ 50</code>,<br />
<code>0 ≤ ids[i] ≤ 10<sup>6</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p>The number that causes a glitch in the test preparing system.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ k ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the total sum of digits in <code>ids</code> is divisible by <code>k</code>, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
