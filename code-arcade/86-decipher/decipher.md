<p>Consider the following ciphering algorithm:</p>
<ul>
<li>For each character replace it with its code.</li>
<li>Concatenate all of the obtained numbers.</li>
</ul>
<p>Given a ciphered string, return the initial one if it is known that it consists only of lowercase letters.</p>
<p><strong>Note:</strong> here the <em>character's code</em> means its decimal ASCII code, the numerical representation of a character used by most modern programming languages.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>cipher = "10197115121"</code>, the output should be<br />
<code>solution(cipher) = "easy"</code>.</p>
<p>Explanation: <code>charCode('e') = 101</code>, <code>charCode('a') = 97</code>, <code>charCode('s') = 115</code> and <code>charCode('y') = 121</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string cipher</strong></p>
<p>A non-empty string which is guaranteed to be a cipher for some other string of lowercase letters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ cipher.length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
