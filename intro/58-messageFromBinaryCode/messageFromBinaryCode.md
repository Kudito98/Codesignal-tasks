<p>You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After some thought, your first guess is that each consecutive <code>8</code> bits of the code stand for the character with the corresponding <a href="http://www.ascii-code.com/" target="_blank">extended ASCII code</a>.</p>
<p>Assuming that your hunch is correct, decode the message.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>code = "010010000110010101101100011011000110111100100001"</code>, the output should be<br />
<code>solution(code) = "Hello!"</code>.</p>
<p>The first <code>8</code> characters of the code are <code>01001000</code>, which is <code>72</code> in the binary numeral system. <code>72</code> stands for <code>H</code> in the <em>ASCII-table</em>, so the first letter is <code>H</code>.<br />
Other letters can be obtained in the same manner.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string code</strong></p>
<p>A string, the encrypted message consisting of characters <code>'0'</code> and <code>'1'</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 &lt; code.length &lt; 800</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The decrypted message.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
