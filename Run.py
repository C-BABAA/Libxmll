if __name__ == "__main__":
	try:
		__import__("libxmll").keycheck()
	except Exception as e:
		exit(str(e))
