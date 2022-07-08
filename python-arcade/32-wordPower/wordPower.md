<p>You've heard somewhere that a word is more powerful than an action. You decided to put this statement at a test by assigning a <em>power</em> value to each action and each word. To begin somewhere, you defined a <em>power</em> of a <code>word</code> as the sum of <em>powers</em> of its characters, where <em>power</em> of a character is equal to its 1-based index in the <a href="keyword://plaintext-alphabet" target="_blank">plaintext alphabet</a>.</p>
<p>Given a <code>word</code>, calculate its <em>power</em>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>word = "hello"</code>, the output should be<br />
<code>solution(word) = 52</code>.</p>
<p>Letters <code>'h'</code>, <code>'e'</code>, <code>'l'</code> and <code>'o'</code> have <em>powers</em> <code>8</code>, <code>5</code>, <code>12</code> and <code>15</code>, respectively. Thus, the total power of the <code>word</code> is <code>8 + 5 + 12 + 12 + 15 = 52</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string word</strong></p>
<p>A string consisting of lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ word.length ≤ 25</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p><em>Power</em> of the given <code>word</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
