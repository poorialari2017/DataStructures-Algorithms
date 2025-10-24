# cpp_runner.py
import subprocess
import sys
import os


class CppRunner:
    def __init__(self):
        self.compilers = ['g++', 'gcc', 'clang++', 'c++']
        self.found_compiler = self._find_compiler()

    def _find_compiler(self):
        """Find available C++ compiler"""
        for compiler in self.compilers:
            try:
                result = subprocess.run([compiler, '--version'],
                                        capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    return compiler
            except:
                continue
        return None

    def run_cpp_code(self, cpp_code, output_filename="output"):
        """Compile and run C++ code - Only show output or full error details"""
        if not self.found_compiler:
            print("Error: No C++ compiler found! Please install g++")
            return False

        try:
            # Create temporary file
            with open(f'{output_filename}.cpp', 'w', encoding='utf-8') as f:
                f.write(cpp_code)

            # Compile
            compile_cmd = [self.found_compiler, f'{output_filename}.cpp', '-o', output_filename]
            if sys.platform == 'win32':
                compile_cmd[-1] = f'{output_filename}.exe'

            compile_result = subprocess.run(compile_cmd, capture_output=True, text=True)

            if compile_result.returncode == 0:
                # Run - Only show output
                run_cmd = [f'./{output_filename}']
                if sys.platform == 'win32':
                    run_cmd = [f'{output_filename}.exe']

                run_result = subprocess.run(run_cmd, capture_output=True, text=True)

                # Only show main output
                print(run_result.stdout)
                return True
            else:
                # If error, only show error
                print("Compilation Error:")
                print(compile_result.stderr)
                return False

        except Exception as e:
            print(f"Runtime Error: {e}")
            return False
        finally:
            # Cleanup completely silent
            self._cleanup(output_filename)

    def _cleanup(self, filename):
        """Clean up temporary files completely silently"""
        files_to_remove = [
            f'{filename}.cpp',
            f'{filename}',
            f'{filename}.exe'
        ]

        for file in files_to_remove:
            if os.path.exists(file):
                try:
                    os.remove(file)
                except:
                    pass  # Completely silent


# Create global instance
cpp_runner = CppRunner()


def run_cpp(cpp_code, output_name="output"):
    """Quick function to run C++ code - Only output or errors"""
    return cpp_runner.run_cpp_code(cpp_code, output_name)